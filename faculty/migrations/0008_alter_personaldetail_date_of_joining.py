# Generated by Django 3.2.7 on 2021-09-20 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0007_alter_personaldetail_total_years'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetail',
            name='Date_of_joining',
            field=models.CharField(max_length=10, null=True),
        ),
    ]