from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_birthdate(birthdate: date):
    today = date.today()
    if birthdate > today:
        raise ValidationError(
            _("%(birthdate)s is not valid"),
            params={'birthdate': birthdate}
        )
