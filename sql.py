from bookclub.models import Author, Book, Reader, BookReading
from django.db.models import Avg, Max, Min, Sum, Count

books = Book.objects.all().select_related('author')
Book.objects.all().values('author', 'title')  # dict, например, для дальнейшей сериализации данных в JSON

Book.objects.all().values_list('author', 'title')  # Список
Book.objects.all().values_list('author', flat=True)  # <QuerySet [1, 2, 2, 2, 3, 4, 4, 5, 6]>

Book.objects.filter(copy_count__gt=1).exclude(author__country='RU')
# TODO-- select_related() ->  ForeignKey, либо OneToOne.
# TODO-- prefetch_related() ->  ManyToMany, и ManyToOne.

'''
Как опознать связь один-ко-многим?
Если у вас есть две сущности спросите себя:
1) Сколько объектов и B могут относится к объекту A?
2) Сколько объектов из A могут относиться к объекту из B?

Если на первый вопрос ответ – множество, а на второй – один (или возможно, что ни одного),
 то вы имеете дело со связью один-ко-многим.'''
'''
Связь многие-ко-многим – это связь, при которой множественным записям из одной таблицы (A)
могут соответствовать множественные записи из другой (B).
'''

# TODO Django может автоматически сгенерировать таблицу для управления отношениями типа ManyToMany.
# TODO Однако если вы хотите, вы можете задать промежуточную таблицу вручную,
# TODO используя аргумент ManyToManyField through.
#
# SELECT "bookclub_book"."id", "bookclub_book"."ISBN",
#        "bookclub_book"."title", "bookclub_book"."description",
#        "bookclub_book"."year_release", "bookclub_book"."copy_count",
#        "bookclub_book"."price", "bookclub_book"."author_id"
# FROM "bookclub_book"
# WHERE "bookclub_book"."author_id" IN (SELECT U0."id"
#                                        FROM "bookclub_author" U0
#                                       WHERE U0."country" = RU)
# -- 7. Сколько стоят все библиотечные книги авторов, у которых больше одной книги?

authors = Author.objects.filter(book_author__copy_count__gt=1)
books = Book.objects.filter(author__in=authors)
books.aggregate(Sum("price"))
