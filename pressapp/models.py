from django.db import models

class InTheNews(models.Model):
  title = models.CharField(max_length=200)
  published_date = models.DateField(null=True, blank=True)
  create_date = models.DateTimeField(auto_now_add=True)
  article_url = models.CharField(max_length=200)
  article_source = models.ManyToManyField('NewsSource', null=True, blank=True)

  def __unicode__(self):
    return self.title

  def source(self):
    return "\n".join([z.source_name for z in self.article_source.all()])

class PressRelease(models.Model):
  title = models.CharField(max_length=200)
  slug = models.SlugField(max_length=100, unique=True, blank=True)
  published_date = models.DateField(null=True, blank=True)
  create_date = models.DateTimeField(auto_now_add=True)
  content = models.TextField(blank=False)

  def __unicode__(self):
    return self.title

class NewsSource(models.Model):
  #need to add image import/upload stuff here..
  source_name = models.CharField(max_length=200)

  class Meta:
    ordering = ["source_name"]

  def __unicode__(self):
    return self.source_name
