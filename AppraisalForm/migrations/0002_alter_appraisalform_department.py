# Generated by Django 3.2.7 on 2021-09-11 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppraisalForm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appraisalform',
            name='department',
            field=models.CharField(choices=[('Basic Science and Humanities', 'Basic Science and Humanities'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil'), ('Computer Science', 'Computer Science'), ('Information Science', 'Information Science'), ('Electronics and Communication', 'Electronics and Communication')], max_length=200, null=True),
        ),
    ]
