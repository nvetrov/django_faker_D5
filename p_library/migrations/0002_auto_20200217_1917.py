# Generated by Django 3.0.3 on 2020-02-17 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Reader',
        ),
        migrations.AddField(
            model_name='book',
            name='reader',
            field=models.ForeignKey(default=-1.0, on_delete=django.db.models.deletion.CASCADE, related_name='Books_Reader', to='p_library.Reader'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='birth_year',
            field=models.SmallIntegerField(verbose_name='Дата рожденья'),
        ),
        migrations.AlterField(
            model_name='author',
            name='country',
            field=models.CharField(max_length=200, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.TextField(verbose_name='Имя автора'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.TextField(verbose_name='название книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year_release',
            field=models.SmallIntegerField(verbose_name='год'),
        ),
    ]