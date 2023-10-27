from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    recipe_name=models.CharField(max_length=100)
    recipe_desc=models.TextField()
    recipe_img=models.ImageField(upload_to="recipes")
    recipe_view_count=models.IntegerField(default=1)


class Department(models.Model):
    department=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class META:
        ordering=["department"]   #It will do the ordering work in ascending order according to department
    

class StudentId(models.Model):
    student_id=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.student_id


class Student(models.Model):
    department=models.ForeignKey(Department,related_name="depart",on_delete=models.CASCADE)
    student_id=models.OneToOneField(StudentId,related_name="studentId",on_delete=models.CASCADE)
    student_name=models.CharField(max_length=100)
    student_email=models.CharField(unique=True,max_length=100)
    student_age=models.IntegerField(default=18)
    student_address=models.TextField()

    def __str__(self) -> str:
        return self.student_name
       

    class META:
        ordering=['student_name']
        verbose_name='student'       






