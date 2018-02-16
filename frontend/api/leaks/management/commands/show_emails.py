from django.core.management.base import BaseCommand
from ...models import Email


class Command(BaseCommand):
    help = 'List all emails'

    def handle(self, *args, **options):
        for email in Email.objects.all():
            print(email.email)
