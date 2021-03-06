# Generated by Django 3.2.7 on 2021-09-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Department', models.CharField(choices=[('Basic Science and Humanities', 'Basic Science and Humanities'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil'), ('Computer Science', 'Computer Science'), ('Information Science', 'Information Science'), ('Electronics and Communication', 'Electronics and Communication')], max_length=200)),
                ('Present_Designation', models.CharField(choices=[('Assistant Professor', 'Assistant Professor'), ('Associate Professor', 'Associate Professor'), ('Professor', 'Professor'), ('Principal', 'Principal'), ('Admin', 'Admin')], max_length=200)),
                ('Whether_HOD', models.BooleanField(default=False)),
                ('Highest_Qualification', models.CharField(max_length=200)),
                ('Recognized_as_a_Research_Guide', models.CharField(max_length=100)),
                ('Years_of_Service_at_MITM', models.DateField()),
                ('Staff_ID', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=50)),
                ('Mail_Id', models.EmailField(max_length=254)),
                ('Contact_No', models.CharField(max_length=10)),
                ('Date_on_which_Acquired', models.CharField(max_length=100)),
                ('Specialization', models.CharField(max_length=100)),
                ('If_yes_Number_of_candidates_being_supervised', models.CharField(max_length=100)),
                ('Previous_Exp', models.DateField()),
                ('total_years', models.IntegerField(null=True)),
            ],
        ),
    ]
