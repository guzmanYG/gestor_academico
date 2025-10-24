from django.db import models

class Student(models.Model):
    matricula = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=150)
    notas = models.JSONField(default=list, blank=True)

    def promedio(self):
        if not self.notas:
            return 0.0
        return round(sum(self.notas) / len(self.notas), 2)

    def __str__(self):
        return f"{self.matricula} - {self.nombre}"
