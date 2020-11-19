from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


class Command(BaseCommand):
    def execute(self, *args, **options):
        admin = get_user_model().objects.create(
            username='admin', is_superuser=True, is_active=True
        )
        admin.set_password('1234qwer')
        admin.save()