# Generated by Django 3.2.7 on 2021-09-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppraisalForm', '0008_auto_20210915_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appraisalform',
            name='a8file',
        ),
        migrations.AlterField(
            model_name='appraisalform',
            name='department',
            field=models.CharField(choices=[('Basic Science and Humanities', 'Basic Science and Humanities'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Information Science and Engineering', 'Information Science and Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Master of Business Administration', 'Master of Business Administration'), ('Master of Computer Applications', 'Master of Computer Applications')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='appraisalform2',
            name='department',
            field=models.CharField(choices=[('Basic Science and Humanities', 'Basic Science and Humanities'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Information Science and Engineering', 'Information Science and Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Master of Business Administration', 'Master of Business Administration'), ('Master of Computer Applications', 'Master of Computer Applications')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='appraisalform3',
            name='department',
            field=models.CharField(choices=[('Basic Science and Humanities', 'Basic Science and Humanities'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Information Science and Engineering', 'Information Science and Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Master of Business Administration', 'Master of Business Administration'), ('Master of Computer Applications', 'Master of Computer Applications')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='grandapiscores',
            name='department',
            field=models.CharField(choices=[('Basic Science and Humanities', 'Basic Science and Humanities'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Information Science and Engineering', 'Information Science and Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Master of Business Administration', 'Master of Business Administration'), ('Master of Computer Applications', 'Master of Computer Applications')], max_length=200, null=True),
        ),
    ]