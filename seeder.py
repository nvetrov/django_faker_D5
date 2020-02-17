# PyDev console: starting.
# Python 3.8.0 (default, Oct 28 2019, 16:14:01)
# [GCC 9.2.1 20191008] on linux
# Django 3.0.3
# import seeder
# from p_library.models import Author, Book
# seeder.seed_all(300, overwrite=True)
'''
1. Сколько автор имеют книг?
2. ПОчему удаляется пароль к БЖ при генирации данных?

'''

# make sure to install faker...
# pip install faker
import datetime
import random
import time

from faker import Faker

# fake = Faker()
fake = Faker('ru_RU')

from django.contrib.auth.models import User  # https://docs.djangoproject.com/en/3.0/topics/auth/default/

# from polls.models import Choice, Poll, Vote
from p_library.models import Author, Book, Reader

user = User.objects.create_user('Admin', 'nvetrov@gmail.com', 'C1vmdpalc34a')
user.save()


def seed_reader(num_entries=10, overwrite=False):
    """
    Creates num_entries worth a new users
    """
    if overwrite:
        print("Overwriting Reader")
        User.objects.all().delete()
        Reader.objects.all().delete()
    count = 0
    for _ in range(num_entries):
        name = fake.name()
        borrowed = str(fake.date_of_birth())
        r = Reader.objects.create(name=name, borrowed=borrowed)
        r.save()
        count += 1
        percent_complete = count / num_entries * 100
        print(
            "Adding {} new Reader: {:.2f}%".format(num_entries, percent_complete),
            end='\r',
            flush=True
        )
    print()


def seed_authors(num_entries=10, overwrite=False):
    """
    Creates num_entries worth a new users
    """
    if overwrite:
        print("Overwriting Users")
        User.objects.all().delete()
        Author.objects.all().delete()
    count = 0
    for _ in range(num_entries):
        full_name = fake.name()  # fake.name(unique=True)
        birth_year = fake.year()
        country = fake.country()
        u = Author.objects.create(full_name=full_name, birth_year=birth_year, country=country)
        u.save()
        count += 1
        percent_complete = count / num_entries * 100
        print(
            "Adding {} new Author: {:.2f}%".format(num_entries, percent_complete),
            end='\r',
            flush=True
        )
    print()


def seed_book(num_entries=10, choice_min=2, choice_max=5, overwrite=False):
    """
    Seeds num_entries poll with random users as owners
    Each Book will be seeded with # choices from choice_min to choice_max
    """
    if overwrite:
        print('Overwriting Book')
        Book.objects.all().delete()
    author = list(Author.objects.all())
    reader = list(Reader.objects.all())
    count = 0
    for _ in range(num_entries):
        p = Book(
            ISBN=fake.isbn10(separator='-'),
            title=fake.words(nb=2, ext_word_list=None, unique=False),  # fake.name(),
            description=fake.sentences(nb=3, ext_word_list=None),  # fake.text(),
            year_release=fake.year(),
            author=random.choice(author),
            reader=random.choice(reader)
        )
        p.save()
        # num_choices = random.randrange(choice_min, choice_max + 1)
        # for _ in range(num_choices):
        #     c = Choice(
        #         poll=p,
        #         choice_text=fake.sentence()
        #     ).save()
        count += 1
        percent_complete = count / num_entries * 100
        print(
            "Adding {} new Book: {:.2f}%".format(num_entries, percent_complete),
            end='\r',
            flush=True
        )
    print()


def seed_all(num_entries=10, overwrite=False):
    """
    Runs all seeder functions. Passes value of overwrite to all
    seeder function calls.
    """
    start_time = time.time()
    # run seeds
    seed_reader(num_entries=num_entries, overwrite=overwrite)
    seed_authors(num_entries=num_entries, overwrite=overwrite)
    seed_book(num_entries=num_entries, overwrite=overwrite)
    # seed_votes()
    # get time
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print("Script Execution took: {} minutes {} seconds".format(minutes, seconds))


# if __name__ == '__main__':
#     print("Populating data..")
#     seed_all()
#     print("Polulating Complate")

