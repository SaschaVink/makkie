# Generated by Django 4.1.1 on 2022-11-20 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_alter_createproject_project_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createproject',
            name='project_name',
            field=models.CharField(max_length=264, unique=True),
        ),
    ]
