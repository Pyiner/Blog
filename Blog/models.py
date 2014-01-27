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
