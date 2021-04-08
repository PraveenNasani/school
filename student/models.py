from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class StudentData(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    grade=models.IntegerField()
    rollno=models.IntegerField(primary_key=True)
    marks=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])

    def __str__(self):
        return self.fname

