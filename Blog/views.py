#coding=utf-8
from django.shortcuts import render_to_response
from Blog.models import Article,Category,OpenProject,FriendUrl
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
import urllib
from django.core.paginator import Paginator
import markdown

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
    category = urllib.unquote(category)
    num = request.GET.get('page')
    if num:
        num = int(num)
    else:
        num=1
    articles = Article.objects.filter(category__name=category).order_by('-id')
    for article in articles:
        article.summary = markdown.markdown(article.summary)
 
    p = Paginator(articles, 5)
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
    articles =Article.objects.all().order_by("-id")
    for article in articles:
        article.summary = markdown.markdown(article.summary)
    p = Paginator(articles, 5)
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
    url = urllib.unquote(url)
    if url:
        try:
            article = Article.objects.get(url = url)
            article.content = markdown.markdown(article.content)
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
    articles = Article.objects.all().order_by('-id')
    for article in articles:
        article.summary = markdown.markdown(article.summary)
    page = []
    for p in articles:
        if key in p.content:
            page.append(p)
    c = GetCategory()
    o = GetOpenProject()
    f = GetFriendUrl()
    h = HotArticle()
    return render_to_response('index.html',{'P':page,'C':c,'Open':o,'Friend':f,'Hotarticle':h})
