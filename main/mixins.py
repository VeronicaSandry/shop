from django.db import models


class ActiveMixin(models.Model):
    is_active = models.BooleanField(
        verbose_name='publicated',
        default=True
    )
    class Meta:
        abstract = True
