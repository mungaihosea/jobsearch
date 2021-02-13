from django.db import models
from django.contrib.auth.models import User

user_model = User

class Job(models.Model):
    title = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100)
    job_type = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    job_description = models.TextField()
    applicants = models.ManyToManyField(user_model, blank = True)


#******Resume files*********
class Interest(models.Model):
    user = models.ForeignKey(user_model, on_delete= models.CASCADE)
    interest = models.CharField(max_length = 100)

class Skill(models.Model):
    user = models.ForeignKey(user_model, on_delete= models.CASCADE)
    skill = models.CharField(max_length= 100)

class Education(models.Model):
    user = models.ForeignKey(user_model, on_delete= models.CASCADE)
    institution = models.CharField(max_length= 100)
    course = models.CharField(max_length= 100)
    since = models.DateField()
    to = models.DateField()

class Experience(models.Model):
    user = models.ForeignKey(user_model, on_delete= models.CASCADE)
    company = models.CharField(max_length= 100)
    job_title = models.CharField(max_length= 100)
    since = models.DateField()
    to = models.DateField()

class Project(models.Model):
    user = models.ForeignKey(user_model, on_delete= models.CASCADE)
    link = models.CharField(max_length= 200)
#******resume files ***********

