# Generated by Django 4.2.2 on 2023-06-28 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='name')),
                ('password', models.CharField(max_length=20, verbose_name='password')),
            ],
        ),
    ]
