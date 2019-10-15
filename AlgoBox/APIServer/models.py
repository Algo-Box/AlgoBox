from django.db import models

# Create your models here.

class contest(models.Model): 
	C_id = models.AutoField(primary_key=True)
	event = models.CharField(max_length=200)
	start = models.DateTimeField()
	end = models.DateTimeField()
	duration = models.IntegerField(default=0)
	href = models.URLField(max_length=200, default="www.codechef.com")
	domain = models.URLField(max_length=200, default="www.codechef.com")
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.event