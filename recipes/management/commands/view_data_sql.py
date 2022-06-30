from django.core.management.base import BaseCommand
from django.db import connection
from recipes.models import Recipe


def MyCSQL():
    with connection.cursor() as c:
        c.execute(
            "SELECT * FROM dbo.recipes_recipe INNER JOIN dbo.auth_user ON dbo.recipes_recipe.author_id=dbo.auth_user.id")
        return c.fetchall()


class Command(BaseCommand):

    help = "Command information"

    def handle(self, *arg, **kwargs):

        # a = Recipe.objects.all().values()
        # a = list(Recipe.objects.prefetch_related(
        #    'author').all().values_list('author'))
        # a = Recipe.objects.raw(
        #   'SELECT * FROM dbo.recipes_recipe INNER JOIN dbo.auth_user ON dbo.recipes_recipe.author_id=dbo.auth_user.id')
        # for s in a:
        # self.stdout.write(self.style.SUCCESS(s))
        #    print(s)
        print(MyCSQL())
