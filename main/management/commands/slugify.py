from django.core.management.base import BaseCommand, CommandError

from main.models import Product

class Command(BaseCommand):
    help_text = 'command for creating slug for products'

    def handle(self, *args, **kwargs):
        queryset = Product.objects.filter(is_active=True)
        for object in queryset:
            try:
                object.save()
            except CommandError as e:
                print(e)
        print('slug created successfuly')