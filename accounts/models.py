from django.db import models

# Create your models here.

class Course(models.Model):
	name = models.CharField(max_length=200, null=True)
	description = models.TextField(max_length=500)
	lectures = models.IntegerField()
	completed_lectures = models.IntegerField()
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Lecture(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	content = models.TextField(max_length=500)

class Quiz(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	question = models.TextField(max_length=500)
	correct_answer = models.TextField(max_length=500)
	wrong_answer1 = models.TextField(max_length=500)
	wrong_answer2 = models.TextField(max_length=500)
