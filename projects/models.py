from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
	
	
	#p1 = Project(
	#	title = 'My First Project',
	#	description = 'A web development project',
	#	technology = 'Django-3.1.1',
	#	image = 'img/project1/png'
	#)
	
	#p2 = Project(
	#	title = 'My Second Project',
	#	description = 'Another web development project',
	#	technology = 'Flask',
	#	image = 'img/project2.png'
	#)
	
	#p3 = Project(
	#	title = 'My Third Project',
	#	description = 'A final development project',
	#	technology = 'Django-3.1.1',
	#	image = 'img/project3.png'
	#)

	
	# p1.image = 'img/project1.png'