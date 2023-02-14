# Generated by Django 4.1.1 on 2022-11-20 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_alter_createproject_project_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadactivity',
            options={'verbose_name': 'Upload activity', 'verbose_name_plural': 'Upload activities'},
        ),
        migrations.RemoveField(
            model_name='uploadactivity',
            name='project',
        ),
        migrations.AddField(
            model_name='uploadactivity',
            name='activities_performed',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AddField(
            model_name='uploadactivity',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='uploadactivity',
            name='date_created_system',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='uploadactivity',
            name='employee_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='upload.createemployee'),
        ),
        migrations.AddField(
            model_name='uploadactivity',
            name='hours_worked',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='uploadactivity',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='activity_fotos'),
        ),
        migrations.AddField(
            model_name='uploadactivity',
            name='image_1_comments',
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
        migrations.AddField(
            model_name='uploadactivity',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='activity_fotos'),
        ),
        migrations.AddField(
            model_name='uploadactivity',
            name='image_2_comments',
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
        migrations.AddField(
            model_name='uploadactivity',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='activity_fotos'),
        ),
        migrations.AddField(
            model_name='uploadactivity',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to='activity_fotos'),
        ),
        migrations.AddField(
            model_name='uploadactivity',
            name='image_4_comments',
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
        migrations.AddField(
            model_name='uploadactivity',
            name='project_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='upload.createproject'),
        ),
        migrations.AlterField(
            model_name='createemployee',
            name='employee_first_name',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='createemployee',
            name='employee_last_name',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='createproject',
            name='project_address',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='createproject',
            name='project_name',
            field=models.CharField(max_length=264, null=True, unique=True),
        ),
    ]