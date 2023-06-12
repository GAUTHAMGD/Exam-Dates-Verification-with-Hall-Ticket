from django.db import models
#from details.models import StudentInfo

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)

    
class HallTicket(models.Model):
    
    exam_date = models.DateField(max_length=20)
    subjects = models.ManyToManyField(Subject)


    def __str__(self):
        return str(self.exam_date)
    # Add any additional fields you need for hall tickets