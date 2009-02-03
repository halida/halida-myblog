from mysite.myblog.models import *

from django.contrib import admin

class ArticleAdmin(admin.ModelAdmin):
    pass
class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog,BlogAdmin)
admin.site.register(Article,ArticleAdmin)

