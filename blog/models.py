from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
lensss = 1000

class Article(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    user = models.ForeignKey(User)

    def  __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text)>lensss:
            return self.text[:lensss]
        else:
            return self.text

class point2(models.Model):
    x = models.FloatField(default=0)
    y = models.FloatField(default=0)
    city = models.CharField(max_length=200,default=0)
    Country = models.CharField(max_length=200,default=0)




