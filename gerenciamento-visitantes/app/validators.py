from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

MAX_BIRTHDATE_FROM_NOW_IN_YEARS = 110
MAX_TICKET_DATE_FROM_NOW_IN_YEARS = 5

def validate_birthdate(birthdate: date):
    today = date.today()

    limit_min_date = date(day=today.day, month=today.month, year=today.year - MAX_BIRTHDATE_FROM_NOW_IN_YEARS)

    if birthdate > today:
        raise ValidationError(
            _("A data de nascimento não pode ser depois da data atual."),
            params={'birthdate': birthdate}
        )

    if birthdate < limit_min_date:
        raise ValidationError(
            _(f"A data limite é de {MAX_BIRTHDATE_FROM_NOW_IN_YEARS} anos atrás ({limit_min_date.strftime('%d/%m/%Y')})"),
            params={'birthdate': birthdate}
        )

def validate_ticket_date(ticket_date: date):
    today = date.today()

    limit_max_date = date(day=today.day, month=today.month, year=today.year + MAX_TICKET_DATE_FROM_NOW_IN_YEARS)

    if ticket_date < today:
        raise ValidationError(
            _("A data da visita não pode ser anterior a data atual."),
            params={'ticket_date': ticket_date}
        )

    if ticket_date > limit_max_date:
        raise ValidationError(
            _(f"A data limite é de {MAX_TICKET_DATE_FROM_NOW_IN_YEARS} anos a partir de agora ({limit_max_date.strftime('%d/%m/%Y')})"),
            params={'ticket_date': ticket_date}
        )
