#coding=utf-8
from django.shortcuts import render_to_response
from Blog.models import Article,Category,OpenProject,FriendUrl
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
import urllib
from django.core.paginator import Paginator

def GetCategory():
    category = Category.objects.all()
    return category

def GetOpenProject():
    openproject = OpenProject.objects.all()
    return openproject

def HotArticle():
    hotarticle = Article.objects.all().order_by('-num')
    num = 0
    h = hotarticle[:]
    hotarticle = []
    for i in h:
        hotarticle.append(i)
        num+=1
        if num==10:
            break
    return hotarticle

def GetFriendUrl():
    friendurl = FriendUrl.objects.all()
    return friendurl


def Categorylist(request,category):
    category = urllib.unquote(str(category))
    category = urllib.unquote(str(category))
    num = request.GET.get('page')
    if num:
        num = int(num)
    else:
        num=1
    article=Article.objects.filter(category__name=category).order_by('-id')
    p = Paginator(article, 5)
    page = p.page(num)
    if num == p.num_pages:
        pnum = None
    else:
        pnum = num+1
    c = GetCategory()
    o = GetOpenProject()
    f = GetFriendUrl()
    h = HotArticle()
    return render_to_response('index.html',{'P':page,'Pnum':pnum,'C':c,'Open':o,'Friend':f,'Hotarticle':h})



def Index(request):
    num = request.GET.get('page')
    if num:
        num = int(num)
    else:
        num=1
    article=Article.objects.all().order_by("-id")
    p = Paginator(article, 5)
    page = p.page(num)
    if num == p.num_pages:
        pnum = None
    else:
        pnum = num+1
    c = GetCategory()
    o = GetOpenProject()
    f = GetFriendUrl()
    h = HotArticle()
    return render_to_response('index.html',{'P':page,'Pnum':pnum,'C':c,'Open':o,'Friend':f,'Hotarticle':h})


def Page(request,url):
    url = urllib.unquote(str(url))
    if url:
        try:
            article = Article.objects.get(url = url)
            Article.objects.filter(url=url).update(num=article.num+1)
            c = GetCategory()
            o = GetOpenProject()
            f = GetFriendUrl()
            h = HotArticle()
            return render_to_response('article.html',{'p':article,'C':c,'Open':o,'Friend':f,'Hotarticle':h})
        except:
            return HttpResponseRedirect('/')
    else:
       return HttpResponseRedirect('/')


def Search(request):
    key = request.GET.get('keywords')
    a = Article.objects.all().order_by('-id')
    page = []
    for p in a:
        if key in p.content:
            page.append(p)
    c = GetCategory()
    o = GetOpenProject()
    f = GetFriendUrl()
    h = HotArticle()
    return render_to_response('index.html',{'P':page,'C':c,'Open':o,'Friend':f,'Hotarticle':h})

def article_out(request):
    from bae.api import bcs
    AK = 'ayEMEGaUU4R8KgSGQYFHhGoX'           #请改为你的AK
    SK = 'la47G8zTiY9STSYpk2Dn2GY0gU7WGfaR'       #请改为你的SK
    bname = 'blog-article'
    bcs2 = bcs.BaeBCS('http://bcs.duapp.com/', AK, SK)
    a = Article.objects.all()
    for i in a:
        ob = str(i.url+'.md')
        o = '/'+ob
        e, d = bcs2.put_object(bname, o,str(i.content))
        bcs2.make_public(bname,o)
    return HttpResponse("Success!")