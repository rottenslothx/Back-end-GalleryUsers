# Generated by Django 3.0.7 on 2020-06-11 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_auto_20200611_1759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Rating', 'verbose_name_plural': 'Ratings'},
        ),
    ]
