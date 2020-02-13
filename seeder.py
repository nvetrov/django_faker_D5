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

from django.contrib.auth.models import User   # https://docs.djangoproject.com/en/3.0/topics/auth/default/

# from polls.models import Choice, Poll, Vote
from p_library.models import Author, Book


# def seed_users(num_entries=10, overwrite=False):
#     """
#     Creates num_entries worth a new users
#     """
#     if overwrite:
#         print("Overwriting Users")
#         Users.objects.all().delete()
#     count = 0
#     for _ in range(num_entries):
#         first_name = fake.first_name()
#         last_name = fake.last_name()
#         u = User.objects.create_user(
#             first_name = first_name,
#             last_name = last_name,
#             email = first_name + "." + last_name + "@fakermail.com",
#             username = first_name + last_name,
#             password="password"
#         )
#         count += 1
#         percent_complete = count / num_entries * 100
#         print(
#                 "Adding {} new Users: {:.2f}%".format(num_entries, percent_complete),
#                 end='\r',
#                 flush=True
#                 )
#     print()
user = User.objects.create_user('sa', 'nvetrov@gmail.com', 'C1vmdpalc34a')
user.save()
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
        full_name = fake.name() #fake.name(unique=True)
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
        print('Overwriting polls')
        Book.objects.all().delete()
    author = list(Author.objects.all())
    count = 0
    for _ in range(num_entries):
        p = Book(
            ISBN=fake.isbn10(separator='-'),  # fake.msisdn(),
            title=fake.words(nb=3, ext_word_list=None, unique=True),  # fake.name(),
            description=fake.sentences(nb=3, ext_word_list=None),  # fake.text(),
            year_release=fake.year(),
            author=random.choice(author)
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


#
# def seed_votes():
#     """
#     Creates a new vote on every poll for every user
#     Voted for choice is selected random.
#     Deletes all votes prior to adding new ones
#     """
#     Vote.objects.all().delete()
#     users = User.objects.all()
#     polls = Poll.objects.all()
#     count = 0
#     number_of_new_votes = users.count() * polls.count()
#     for poll in polls:
#         choices = list(poll.choice_set.all())
#         for user in users:
#             v = Vote(
#                 user=user,
#                 poll=poll,
#                 choice=random.choice(choices)
#             ).save()
#             count += 1
#             percent_complete = count / number_of_new_votes * 100
#             print(
#                 "Adding {} new votes: {:.2f}%".format(number_of_new_votes, percent_complete),
#                 end='\r',
#                 flush=True
#             )
#     print()


def seed_all(num_entries=10, overwrite=False):
    """
    Runs all seeder functions. Passes value of overwrite to all
    seeder function calls.
    """
    start_time = time.time()
    # run seeds
    seed_authors(num_entries=num_entries, overwrite=overwrite)
    seed_book(num_entries=num_entries, overwrite=overwrite)
    # seed_votes()
    # get time
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print("Script Execution took: {} minutes {} seconds".format(minutes, seconds))


if __name__ == '__main__':
    print("Populating data..")
    seed_all()
    print("Polulating Complate")
