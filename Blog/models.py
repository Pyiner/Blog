#coding=utf-8
from django.db import models
from django.contrib import admin


class Article(models.Model):
    title = models.CharField(max_length=64)
    url = models.CharField(max_length=64)
    date = models.DateTimeField()
    content = models.TextField()
    summary = models.TextField()
    category = models.ForeignKey('Category')
    label = models.ManyToManyField('Label')
    num = models.IntegerField(default=0)
    def __unicode__(self):
        return self.title


class Label(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name


class OpenProject(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()
    def __unicode__(self):
        return self.name


class FriendUrl(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()
    def __unicode__(self):
        return self.name


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','date','url')
    filter_horizontal = ('label',)


class LabelAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class OpenProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

class FriendUrlAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Article,ArticleAdmin)
admin.site.register(Label,LabelAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(OpenProject,OpenProjectAdmin)
admin.site.register(FriendUrl,FriendUrlAdmin)


from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Article)#保存文章的时候自动将文章上传到百度云存储
def article_out(sender,instance,**kwargs):
    from bae.api import bcs
    AK = ''           #请改为你的AK
    SK = ''       #请改为你的SK
    bname = 'blog-article'
    bcs2 = bcs.BaeBCS('http://bcs.duapp.com/', AK, SK)
    ob = str(instance.url+'.md')
    o = '/'+ob
    e, d = bcs2.put_object(bname, o,str(instance.content))
    bcs2.make_public(bname,o) 
