from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_birthdate(birthdate: date):
    today = date.today()
    if birthdate > today:
        raise ValidationError(
            _("Data de nascimento inválida"),
            params={'birthdate': birthdate}
        )

def validate_ticket_date(ticket_date: date):
    today = date.today()
    if ticket_date < today:
        raise ValidationError(
            _("A data da visita não pode ser antes da data atual"),
            params={'ticket_date': ticket_date}
        )
