from django.db import models

class Task(models.Model):

    nomTarea = models.CharField(max_length=250)
    descrip = models.CharField(max_length=250)
    hecha = models.BooleanField(default=False)
    
    def __str__(self):

        return self.nomTarea