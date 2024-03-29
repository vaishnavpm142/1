# Generated by Django 4.0.2 on 2023-08-19 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(blank=True, default='user', max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('status', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'db_table': 'useraccount',
            },
        ),
    ]
