# Generated by Django 3.2.13 on 2022-10-11 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('summary', models.TextField()),
                ('running_time', models.IntegerField()),
            ],
        ),
    ]
