# Generated by Django 3.0.3 on 2020-02-17 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0008_auto_20200217_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Books_Reader', to='p_library.Reader'),
        ),
    ]
