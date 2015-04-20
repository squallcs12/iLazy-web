from django.core.management.base import NoArgsCommand
from accounts.models import User


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        if not User.objects.filter(username='admin').count():
            User.objects.create_superuser('admin', 'bang.dao@eastagile.com', 'admin123')
