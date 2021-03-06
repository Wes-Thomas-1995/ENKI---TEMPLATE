# Generated by Django 4.0.1 on 2022-01-11 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=80)),
                ('phone_nbr', models.CharField(blank=True, max_length=11, null=True)),
                ('firm', models.CharField(max_length=80)),
                ('permission', models.PositiveSmallIntegerField(choices=[(0, 'ENKI Ultimate User'), (1, 'Administrative Superuser'), (2, 'Company Superuser'), (3, 'Mid-Level User'), (4, 'Junior User')], default=0)),
            ],
        ),
    ]
