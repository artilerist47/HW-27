from pathlib import Path
from django.core.management.base import BaseCommand
from ads.models import Category, Ad, Location, User
from ads.management.data.csv_to_json import load_csv_as_json

JSONS_PATH = Path(__file__).parent.parent.absolute().joinpath('data', 'data')
CATEGORIES_FILE_CSV = JSONS_PATH.joinpath('category.csv')
ADVERTISEMENTS_FILE_CSV = JSONS_PATH.joinpath('ad.csv')
LOCATIONS_FILE_CSV = JSONS_PATH.joinpath('location.csv')
USERS_FILE_CSV = JSONS_PATH.joinpath('user.csv')


class Command(BaseCommand):
    def import_categories(self):
        data = load_csv_as_json(CATEGORIES_FILE_CSV)

        for item in data:
            item.pop('id')

            new_category = Category()
            [setattr(new_category, key, value) for key, value in item.items()]
            new_category.save()
        print('Categories was imported')

    def import_advertisements(self):
        data = load_csv_as_json(ADVERTISEMENTS_FILE_CSV)

        for item in data:
            item.pop('id')

            new_ad = Ad()
            [setattr(new_ad, key, value) for key, value in item.items()]
            new_ad.save()
        print('Advertisements was imported')

    def import_locations(self):
        data = load_csv_as_json(LOCATIONS_FILE_CSV)

        for item in data:
            item.pop('id')

            new_ad = Location()
            [setattr(new_ad, key, value) for key, value in item.items()]
            new_ad.save()
        print('Locations was imported')

    def import_users(self):
        data = load_csv_as_json(USERS_FILE_CSV)
        for item in data:
            item.pop('id')

            new_ad = User()
            [setattr(new_ad, key, value) for key, value in item.items()]
            new_ad.save()
        print('Users was imported')


    def handle(self, *args, **options):
        self.import_locations()
        self.import_categories()
        self.import_users()
        self.import_advertisements()