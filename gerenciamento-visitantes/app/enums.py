from django.db import models

class TicketType(models.IntegerChoices):
    NORMAL = 1, 'Normal'
    VIP = 2, 'VIP'
    PREMIUM = 3, 'Premium'
