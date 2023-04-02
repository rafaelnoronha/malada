from django.db import models


YES_NO_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No'),
)


class Base(models.Model):
    active = models.CharField(
        verbose_name='Active',
        max_length=1,
        choices=YES_NO_CHOICES,
        default='Y'
    )

    dma_created = models.DateField(
        verbose_name='Creation date',
        auto_now_add=True
    )

    hms_created = models.TimeField(
        verbose_name='Creation time',
        auto_now_add=True
    )

    dma_alteration = models.DateField(
        verbose_name='Alteration date',
        auto_now=True
    )

    hms_alteration = models.TimeField(
        verbose_name='Alteration time',
        auto_now=True
    )

    
    class Meta:
        abstract = True
