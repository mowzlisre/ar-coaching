from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
	CHOICES=(('PG-TRB','PG-TRB'),('POLY-TRB','POLY-TRB'),('ENGR-TRB','ENGR-TRB'),('TNSET','TNSET'),('GATE','GATE'))
	title = models.CharField(max_length=255)
	content = RichTextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	tag =  models.CharField(max_length=255, choices=CHOICES, null=False)
	link = models.CharField(max_length=255, blank=True)
	def __str__(self):
		return self.title

class Announcement(models.Model):
	announcement = models.TextField(max_length=500)
	time = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.announcement
