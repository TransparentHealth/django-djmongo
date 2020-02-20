# Generated by Django 3.0.3 on 2020-02-18 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djmongo_read', '0002_new_output_formats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customhttpauthreadapi',
            name='output_format',
            field=models.CharField(choices=[('json', 'JSON (.json)'), ('ndjson', 'NDJSON (.ndjson)'), ('csv', 'Comma Separated Value (.csv)'), ('txt', 'Tab-Delimited (.txt)'), ('html', 'HTML (.html)')], default='json', max_length=6),
        ),
        migrations.AlterField(
            model_name='customipauthreadapi',
            name='output_format',
            field=models.CharField(choices=[('json', 'JSON (.json)'), ('ndjson', 'NDJSON (.ndjson)'), ('csv', 'Comma Separated Value (.csv)'), ('txt', 'Tab-Delimited (.txt)'), ('html', 'HTML (.html)')], default='json', max_length=6),
        ),
        migrations.AlterField(
            model_name='customoauth2readapi',
            name='output_format',
            field=models.CharField(choices=[('json', 'JSON (.json)'), ('ndjson', 'NDJSON (.ndjson)'), ('csv', 'Comma Separated Value (.csv)'), ('txt', 'Tab-Delimited (.txt)'), ('html', 'HTML (.html)')], default='json', max_length=6),
        ),
        migrations.AlterField(
            model_name='customoauth2readapi',
            name='sort',
            field=models.TextField(blank=True, default='', help_text='e.g. [["somefield", 1], ["someotherfield", -1] ]', max_length=2048, verbose_name='Sort Dictionary'),
        ),
        migrations.AlterField(
            model_name='custompublicreadapi',
            name='output_format',
            field=models.CharField(choices=[('json', 'JSON (.json)'), ('ndjson', 'NDJSON (.ndjson)'), ('csv', 'Comma Separated Value (.csv)'), ('txt', 'Tab-Delimited (.txt)'), ('html', 'HTML (.html)')], default='json', max_length=6),
        ),
    ]
