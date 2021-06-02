from django.db import models

# Create your models here.
class Blog(models.Model):
	"""docstring for Evnt"""
	blog_image = models.ImageField(upload_to="event_images/")
	blog_text = models.TextField()
	blog_title = models.CharField(max_length=300)
	blog_date = models.DateTimeField()

	def get_summary(self):
		return self.blog_text[:70]

	def __str__(self):
		return self.blog_title