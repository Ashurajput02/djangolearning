from django.db import models
from django.utils import timezone
# Create your models here.


class chaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'Masala'),
        ('GR', 'Ginger'),
        ('KL', 'Kiwi'),
        ('PL', 'Plain'),
        ('EL', 'Elaichi'),
    ]
    name = models.CharField(max_length=100)
    # yeh folder jahan data jaana hai yeh mujhe configure karna padega
    image = models.ImageField(upload_to='chais/')
    # maine default add karna hai  isliye time zone ki jaroorat padi
    date_added = models.DateTimeField(default=timezone.now)
    # chai ki type rakhne ke liye
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)

# yeh function voh object ke naam ko change karne ke liye


def __str__(self):
    return self.name
