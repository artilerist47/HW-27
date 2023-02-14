import json
from pathlib import Path
from django.core.management.base import BaseCommand
from ads.models import Category, Ad
from ads.management.data.csv_to_json import compile_jsons


JSONS_PATH = Path(__file__).parent.parent.absolute().joinpath('data', 'data')
CATEGORIES_FILE = JSONS_PATH.joinpath('categories.json')
ADVERTISEMENTS_FILE = JSONS_PATH.joinpath('ads.json')

class Command(BaseCommand):
    def import_categories(self):
        with open(CATEGORIES_FILE, 'r', encoding='utf-8') as file:
            file_data = file.read()
            data = json.loads(file_data)

        for item in data:
            item.pop('id')

            new_category = Category()
            [setattr(new_category, key, value) for key, value in item.items()]
            new_category.save()
        print('Categories was imported')

    def import_advertisements(self):
        with open(ADVERTISEMENTS_FILE, 'r', encoding='utf-8') as file:
            file_data = file.read()
            data = json.loads(file_data)

        for item in data:
            item.pop('id')

            new_ad = Ad()
            [setattr(new_ad, key, value) for key, value in item.items()]
            new_ad.save()
        print('Advertisements was imported')


    def handle(self, *args, **options):
        compile_jsons()
        self.import_categories()
        self.import_advertisements()