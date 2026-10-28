from django.db import models
from .enums import TicketType
from .validators import validate_birthdate


class Visitor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True, error_messages={'unique': 'Este CPF já está cadastrado.'})
    birthdate = models.DateField(validators=[validate_birthdate])
    ticket_date = models.DateField()
    ticket_type = models.IntegerField(choices=TicketType.choices)
    ticket_code = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
