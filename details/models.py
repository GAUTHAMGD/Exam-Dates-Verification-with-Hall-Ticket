from django.db import models

class Exam(models.Model):
    subject = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.subject

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    exams = models.ManyToManyField(Exam, through='HallTicket')

    def __str__(self):
        return self.name

class HallTicket(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    hall_ticket_number = models.CharField(max_length=20)

    def __str__(self):
        return self.hall_ticket_number
