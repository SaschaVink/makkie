# Generated by Django 4.1.1 on 2022-11-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=264, unique=True)),
                ('project_address', models.CharField(max_length=264, unique=True)),
                ('project_description', models.CharField(blank=True, max_length=264, null=True)),
            ],
        ),
    ]