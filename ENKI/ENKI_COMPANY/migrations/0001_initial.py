# Generated by Django 4.0.1 on 2022-01-29 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child_Company_Information',
            fields=[
                ('child_company_name', models.CharField(blank=True, max_length=200, null=True)),
                ('child_company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Parent_Company_Information',
            fields=[
                ('parent_company_name', models.CharField(max_length=200)),
                ('parent_company_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Client_Directory',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=200)),
                ('client_email', models.CharField(max_length=200)),
                ('client_telephone', models.CharField(max_length=200)),
                ('client_address', models.CharField(max_length=200)),
                ('client_postcode', models.CharField(max_length=200)),
                ('point_of_contact_first', models.CharField(max_length=200)),
                ('point_of_contact_last', models.CharField(max_length=200)),
                ('account_status', models.BooleanField(default=True)),
                ('child_company_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ENKI_COMPANY.child_company_information')),
            ],
        ),
        migrations.AddField(
            model_name='child_company_information',
            name='parent_company_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ENKI_COMPANY.parent_company_information'),
        ),
    ]
