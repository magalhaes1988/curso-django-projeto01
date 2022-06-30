from random import randint

import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker
from recipes.models import Category, Recipe

CATEGORIES = [
    "Cafe da Manha",
    "Lanches",
    "Cafe da tarde",
    "Almoco",
    "Jantar",
    "Doces",
    "Pao"
]


class Provider(faker.providers.BaseProvider):

    def recipes_category(self):
        return self.random_element(CATEGORIES)


class Command(BaseCommand):

    help = "Command information"

    def handle(self, *arg, **kwargs):

        fake = Faker("pt_BR")
        fake.add_provider(Provider)

        # print(fake.recipes_category())

        for _ in range(7):

            d = fake.unique.recipes_category()
            Category.objects.create(name=d)

        check_category = Category.objects.all().count()
        self.stdout.write(self.style.SUCCESS(
            f"Number of Category: {check_category}"))

        for _ in range(7):

            c_title = fake.sentence(nb_words=6)
            c_description = fake.sentence(nb_words=12)
            c_preparation_time = fake.random_number(digits=2, fix_len=True)
            c_preparation_time_unit = 'Minutos'
            c_servings = fake.random_number(digits=2, fix_len=True)
            c_servings_unit = 'Porção'
            c_preparation_step = fake.text(3000)
            c_author_id = 1
            c_category_id = randint(1, 7)

            Recipe.objects.create(
                title=c_title,
                description=c_description,
                preparation_time=c_preparation_time,
                preparation_time_unit=c_preparation_time_unit,
                servings=c_servings,
                servings_unit=c_servings_unit,
                preparation_steps=c_preparation_step,
                author_id=c_author_id,
                category_id=c_category_id)

        check_recipes = Recipe.objects.all().count()
        self.stdout.write(self.style.SUCCESS(
            f"Number of Recipes: {check_recipes}"))
