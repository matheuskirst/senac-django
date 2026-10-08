from django.db import models

class Visitor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    birthdate = models.DateField()
    ticket_date = models.DateField()
    ticket_type = models.IntegerField()
    ticket_code = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
