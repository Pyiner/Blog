from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from Blog.models import Article
import markdown
from django.utils import feedgenerator

class LatestEntriesFeed(Feed):
    title = "Yiner in Python"
    link = "http://www.pyiner.com/"
    description = "Yiner in Python"
    def items(self):
        return Article.objects.order_by('-id')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return markdown.markdown(item.content)

    def item_link(self, item):
         return self.link+item.url+'/'