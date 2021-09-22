# Generated by Django 3.2.7 on 2021-09-11 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppraisalForm', '0003_auto_20210911_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='appraisalform',
            name='a10file',
            field=models.FileField(null=True, upload_to='quantitative'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='a11file',
            field=models.FileField(null=True, upload_to='quantitative'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='a12file',
            field=models.FileField(null=True, upload_to='quantitative'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='a15file',
            field=models.FileField(null=True, upload_to='quantitative'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='a8bfile',
            field=models.FileField(null=True, upload_to='quantitative'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='a8file',
            field=models.FileField(null=True, upload_to='quantitative'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='a9file',
            field=models.FileField(null=True, upload_to='quantitative'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='b10file',
            field=models.FileField(null=True, upload_to='quantitative'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='b11file',
            field=models.FileField(null=True, upload_to='quantitative'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='b12file',
            field=models.FileField(null=True, upload_to='quantitative'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='b8bfile',
            field=models.FileField(null=True, upload_to='quantitative'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='b8file',
            field=models.FileField(null=True, upload_to='quantitative'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='c10file',
            field=models.FileField(null=True, upload_to='quantitative'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='c14file',
            field=models.FileField(null=True, upload_to='quantitative'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='c8file',
            field=models.FileField(null=True, upload_to='quantitative'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='c9file',
            field=models.FileField(null=True, upload_to='quantitative'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='d8bfile',
            field=models.FileField(null=True, upload_to='quantitative'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='percent1',
            field=models.FileField(null=True, upload_to='passpercents'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='percent2',
            field=models.FileField(null=True, upload_to='passpercents'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='percent3',
            field=models.FileField(null=True, upload_to='passpercents'),
        ),
        migrations.AddField(
            model_name='appraisalform',
            name='percent4',
            field=models.FileField(null=True, upload_to='passpercents'),
        ),
    ]
