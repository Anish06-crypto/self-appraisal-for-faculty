# Generated by Django 3.2.7 on 2021-09-15 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppraisalForm', '0007_auto_20210915_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrandApiScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=10, null=True)),
                ('department', models.CharField(choices=[('Basic Science and Humanities', 'Basic Science and Humanities'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil'), ('Computer Science', 'Computer Science'), ('Information Science', 'Information Science'), ('Electronics and Communication', 'Electronics and Communication')], max_length=200, null=True)),
                ('designation', models.CharField(choices=[('Assistant Professor', 'Assistant Professor'), ('Associate Professor', 'Associate Professor'), ('Professor', 'Professor')], max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('grade', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], max_length=2, null=True)),
                ('whether_HOD', models.BooleanField(default=False)),
                ('submitted_Faculty', models.BooleanField(default=False)),
                ('submitted_HOD', models.BooleanField(default=False)),
                ('submitted_Principal', models.BooleanField(default=False)),
                ('Part1APIscore', models.BigIntegerField(default=0, null=True)),
                ('Part1HODAPIscore', models.BigIntegerField(default=0, null=True)),
                ('Part1PAPIscore', models.BigIntegerField(default=0, null=True)),
                ('part2APIscore', models.BigIntegerField(default=0, null=True)),
                ('part2HODAPIscore', models.BigIntegerField(default=0, null=True)),
                ('part2PAPIscore', models.BigIntegerField(default=0, null=True)),
                ('part3APIscore', models.BigIntegerField(default=0, null=True)),
                ('part3HODAPIscore', models.BigIntegerField(default=0, null=True)),
                ('part3PAPIscore', models.BigIntegerField(default=0, null=True)),
                ('GrandScore', models.BigIntegerField(default=0, null=True)),
                ('GrandScoreHOD', models.BigIntegerField(default=0, null=True)),
                ('GrandScoreP', models.BigIntegerField(default=0, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='appraisalform',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='appraisalform2',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='appraisalform3',
            name='GrandScore',
        ),
        migrations.RemoveField(
            model_name='appraisalform3',
            name='GrandScoreHOD',
        ),
        migrations.RemoveField(
            model_name='appraisalform3',
            name='GrandScoreP',
        ),
        migrations.RemoveField(
            model_name='appraisalform3',
            name='grade',
        ),
    ]
