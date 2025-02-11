"""
Django Command to wait for DB
"""
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

import time
from psycopg2 import OperationalError as Psycopg2OpError


class Command(BaseCommand):
    """Management command to wait for DB setup"""

    def handle(self, *args, **options):
        """Entrypoint For command"""
        self.stdout.write('Waiting for Database...')
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Successfully connected \
                                             to Database'))
