# Generated by Django 3.2.7 on 2021-09-17 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppraisalForm', '0012_auto_20210917_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backupapiscores',
            name='academic_year',
            field=models.IntegerField(choices=[('2021', '2021'), ('2022', '2022'), ('2023', '2023')], null=True),
        ),
    ]
