# Generated by Django 2.0.1 on 2018-02-27 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('jobstories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobstories',
            name='category',
            field=models.ForeignKey(default=2, on_delete=False, to='main.Category'),
            preserve_default=False,
        ),
    ]
