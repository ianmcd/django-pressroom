from django.contrib import admin
from pressapp.models import InTheNews, PressRelease, NewsSource

class NewsAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['title', 'published_date']}),
    ('Source Details', {'fields': ['article_url', 'article_source']})
  ]

  list_display = ('title', 'source_name', 'published_date')
  search_fields = ['title']


class PressAdmin(admin.ModelAdmin):
  list_display = ('title', 'published_date')
  search_fields = ['title']
  prepopulated_fields = {'slug': ('title',), }


class SourceAdmin(admin.ModelAdmin):
  search_fields = ['source_name']

admin.site.register(InTheNews, NewsAdmin)
admin.site.register(PressRelease, PressAdmin)
admin.site.register(NewsSource, SourceAdmin)
