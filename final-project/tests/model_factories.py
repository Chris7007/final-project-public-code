import factory
from random import randint
from random import choice
from models import *

last_name = factory.Sequence(lambda n: n + 1)


class UserFactory(factory.django.DjangoModelFactory):
    # name each field and provide dummy data
    username = factory.Faker('sentence', nb_words=1)
    password = 'django123'
    first_name = factory.Faker('sentence', nb_words=1)
    last_name = factory.Faker('sentence', nb_words=1)
    email = factory.Faker('sentence', nb_words=1)
    is_staff = False
    date_joined = '2024-12-02T00:00:00Z'
    last_login = '2024-12-07T00:00:00Z'
    
    class Meta:
        model = User


class UserProfileFactory(factory.django.DjangoModelFactory):
    # name each field and provide dummy data
    # user = factory.SubFactory(UserFactory)
    is_verified = True
    country = 'United Kingdom'
    region = 'London'
    age = randint(18, 80)
    gender = choice(['male', 'female'])
    professional_status = choice(['Hobbyist', 'Student', 'Graduate', 'Professional'])

    class Meta:
        model = UserProfile





