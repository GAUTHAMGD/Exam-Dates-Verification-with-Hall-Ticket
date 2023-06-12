from django.db import models
from Registration.models import BaseModel, User
from django.db.models import DateField

class StudentInfo(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class ExamInfo(StudentInfo):
    Subjects = models.ManyToManyField('Subject')
   
    
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name  
# class Exam(models.Model):
#    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
#    subject = models.ForeignKey(ExamInfo, on_delete=models.CASCADE)
   
#    class Meta:
#        verbose_name_plural = "Student Info"
