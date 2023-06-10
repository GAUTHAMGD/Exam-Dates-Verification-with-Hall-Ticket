from django.db import models
from details.models import StudentInfo


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    exam_date = models.DateField()
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    



class HallTicket(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    hall_ticket_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Hall Ticket: {self.hall_ticket_number} - Student: {self.student} - Subject: {self.subject}"

