# Generated by Django 3.0.3 on 2020-02-16 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20200212_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True, verbose_name='Кому одолжил(Имя)')),
                ('borrowed', models.DateField(blank=True, null=True, verbose_name='Дата выдачи книги')),
            ],
        ),
    ]
