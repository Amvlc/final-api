import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from reviews.models import Category, Comment, Genre, Review, Title, User

TABLES_DICT = {
    User: 'users.csv',
    Category: 'category.csv',
    Genre: 'genre.csv',
    Title: 'titles.csv',
    Review: 'review.csv',
    Comment: 'comments.csv',
}


class Command(BaseCommand):
    help = 'Import data from csv files'

    def handle(self, *args, **kwargs):
        for model, file in TABLES_DICT.items():
            with open(
                os.path.join(settings.BASE_DIR, 'static/data/', file),
                'r',
                encoding='utf-8'
            ) as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    model.objects.create(**row)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
