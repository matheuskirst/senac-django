from django.forms import Form, ModelForm
from .models import Visitor

class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        fields = [
            'first_name',
            'last_name',
            'cpf',
            'birthdate',
            'ticket_date',
            'ticket_type'
        ]
