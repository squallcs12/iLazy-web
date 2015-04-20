from datetime import timedelta
from django.utils import timezone
from accounts.factories import UserFactory
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
    price = factory.Sequence(lambda n: fake.random_int(max=999))
    price_life = factory.LazyAttribute(lambda o: fake.random_int(max=999) + o.price)
    command = factory.Sequence(lambda n: fake.lexify(text="??????????"))


class UserAppFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.UserApp
        django_get_or_create = ('user', 'app')

    user = factory.SubFactory(UserFactory)
    app = factory.SubFactory(AppFactory)
    expires = factory.Sequence(lambda n: timezone.now().date() + timedelta(days=30))

