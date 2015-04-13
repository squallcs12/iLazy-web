from api import models
import factory
import faker


fake = faker.Faker()


SITES = [
    'google.com',
    'twitter.com',
    'facebook.com',
    'skype.com',
    'longdomainnam.com',
]


class AppFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.App
        django_get_or_create = ('name', 'site')

    name = factory.Sequence(lambda n: "App nam %s" % n)
    site = factory.Sequence(lambda n: SITES[n % len(SITES)])
    price = factory.Sequence(lambda n: fake.random_int(max=999) + fake.random_int(min=10, max=99) / 100.)
