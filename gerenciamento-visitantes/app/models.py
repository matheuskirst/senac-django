from django.db import models
from .validators import validate_birthdate


class Visitor(models.Model):
    class TicketType(models.IntegerChoices):
        NORMAL = 1, 'Normal'
        VIP = 2, 'VIP'
        PREMIUM = 3, 'Premium'
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    birthdate = models.DateField(validators=[validate_birthdate])
    ticket_date = models.DateField()
    ticket_type = models.IntegerField(choices=TicketType.choices)
    ticket_code = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
