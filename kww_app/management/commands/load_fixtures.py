from django.core.management.base import BaseCommand
import factory
from django.db.models import signals
from django.core.management import call_command
from django.db import connection


class Command(BaseCommand):
    help = 'load fixtures while disabling signals'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str)

    def handle(self, *args, **options):
        fixture_file = options['file']
        self.load_fixture(fixture_file)

    @factory.django.mute_signals(signals.pre_save, signals.post_save)
    def load_fixture(self, fixture_file):
        with connection.cursor() as cursor:
            cursor.execute('SET session_replication_role TO \'replica\'')
        call_command('loaddata', fixture_file, verbosity=3, app_label='*')
        with connection.cursor() as cursor:
            cursor.execute('SET session_replication_role TO \'origin\'')

