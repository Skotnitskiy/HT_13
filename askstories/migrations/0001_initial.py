# Generated by Django 2.0.1 on 2018-02-27 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Askstories',
            fields=[
                ('by', models.CharField(blank=True, max_length=100, null=True)),
                ('descendants', models.CharField(blank=True, max_length=15, null=True)),
                ('id', models.TextField(blank=True, primary_key=True, serialize=False, unique=True)),
                ('kids', models.TextField(blank=True, null=True)),
                ('score', models.CharField(blank=True, max_length=20, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('time', models.TextField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
