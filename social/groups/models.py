from django.db import models
from django.utils.text import slugify #this fills empty spaces with _ to make urls


import misaka #can put links / Mark-down text

from django.contrib.auth import get_user_model #returns user model that is currently active in project
User=get_user_model() #call things off current user's session
from django.urls import reverse

from django import template
register = template.Library() #helps us to use custom template tags, user_group related name allows to connect from post to group member

#Main Model

class Group(models.Model):
    name = models.CharField(max_length = 225, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships', on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name = 'user_groups', on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')
