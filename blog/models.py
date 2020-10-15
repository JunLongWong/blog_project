from django.db import models

#Category Table
class Category(models.Model):
		name = models.CharField(max_length=20)

#Post Table
class Post(models.Model):
		title = models.CharField(max_length=256)
		body = models.TextField()
		created_on = models.DateTimeField(auto_now_add=True)
		last_modified = models.DateTimeField(auto_now=True)
		categories = models.ManyToManyField('Category', related_name='posts')

#Comment Table
class Comment(models.Model):
	author = models.CharField(max_length=60)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	# many comments can be assigned to one post.
	post = models.ForeignKey('Post',on_delete=models.CASCADE)