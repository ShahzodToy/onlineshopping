from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
class Coupon(models.Model):
    code = models.CharField(max_length=50)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],
                                   help_text='Create as persentage (0:100)')
    active = models.BooleanField()

    def __str__(self):
        return f'{self.discount}'

    

