# Generated by Django 3.0.7 on 2020-06-11 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(blank=True, default='eiei', max_length=100),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_text',
            field=models.CharField(blank=True, default='eiei', max_length=100),
        ),
    ]
