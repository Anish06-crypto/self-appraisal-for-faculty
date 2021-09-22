# Generated by Django 3.2.7 on 2021-09-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppraisalForm', '0009_auto_20210915_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='appraisalform',
            name='No_of_students1_hod',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='No_of_students2_hod',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='No_of_students3_hod',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='No_of_students4_hod',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='Percent_over_601_hod',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='Percent_over_602_hod',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='Percent_over_603_hod',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='Percent_over_604_hod',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='Percentage_of_pass1_hod',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='Percentage_of_pass2_hod',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='Percentage_of_pass3_hod',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='Percentage_of_pass4_hod',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='Sub_code1_hod',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='Sub_code2_hod',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='Sub_code3_hod',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='Sub_code4_hod',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
    ]
