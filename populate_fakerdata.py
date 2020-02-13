import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookclub.settings')

import django

django.setup()

import random

from p_library.models import Author, Book

from faker import Faker

fake = Faker()

# fake = Faker('ru_RU')

full_name = fake.name()
birth_year = fake.year()
country = fake.country()[2]


def add_author():
    s = Author.objects.get_or_create(full_name=full_name, birth_year=birth_year, country=country)[0]
    return s.save()


def populate(N=3):
    for entry in range(N):
        # author = add_author()
        # full_name = fake.name()
        # birth_year = fake.year()
        # country = fake.country()

        full_name = fake.name()
        birth_year = fake.year()
        country = fake.country()[2]

        ISBN = fake.isbn10(separator='-')
        title = fake.words(nb=3, ext_word_list=None, unique=True)  #fake.word(ext_word_list=None)
        description = fake.sentences(nb=3, ext_word_list=None)
        year_release = fake.year()
    book = Book.objects.get_or_create(ISBN=ISBN, title=title, description=description, year_release=year_release)
    return book.save


if __name__ == '__main__':
    print("Populating data..")
    populate(20)
    print("Polulating Complate")
