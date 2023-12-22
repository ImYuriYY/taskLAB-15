from django.db import models



class Subject(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class Score(models.Model):
    value = models.IntegerField()
    def __str__(self):
        return f'{self.value}'




class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    subj = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.ForeignKey(Score, on_delete=models.CASCADE)
    gpa = models.FloatField()


    def __str__(self):
        return self.name

