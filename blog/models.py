from django.db import models

# Create your models here.
class Blog(models.Model):
	"""docstring for Evnt"""
	blog_image = models.ImageField(upload_to="event_images/")
	blog_text = models.TextField()
	blog_title = models.CharField(max_length=300)
	blog_date = models.DateTimeField()