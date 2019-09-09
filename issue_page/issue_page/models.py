from django.db import models


class Issue(models.Model):
    name = models.SlugField(primary_key=True)
    text = models.TextField()


