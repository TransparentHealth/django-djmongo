# Generated by Django 2.2.4 on 2019-11-05 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='WriteAPIOAuth2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scopes', models.CharField(blank=True, default='*', help_text='Space delimited list of scopes required. * means no scope is required.', max_length=1024)),
                ('http_post', models.BooleanField(blank=True, default=True)),
                ('http_put', models.BooleanField(blank=True, default=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('database_name', models.CharField(max_length=100)),
                ('collection_name', models.CharField(max_length=100)),
                ('json_schema', models.TextField(default='{}', help_text='Default "{}", means no JSON Schema.', max_length=20480, verbose_name='JSON Schema')),
                ('readme_md', models.TextField(blank=True, default='', max_length=4096)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Write API with OAuth2 Auth',
                'verbose_name_plural': 'Write APIs with OAuth2 Auth',
                'ordering': ('-creation_date',),
                'get_latest_by': 'creation_date',
            },
        ),
        migrations.CreateModel(
            name='WriteAPIIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('http_post', models.BooleanField(blank=True, default=True)),
                ('http_put', models.BooleanField(blank=True, default=True)),
                ('database_name', models.CharField(max_length=100)),
                ('collection_name', models.CharField(max_length=100)),
                ('json_schema', models.TextField(default='{}', help_text='Default "{}", means no JSON Schema.', max_length=20480, verbose_name='JSON Schema')),
                ('from_ip', models.TextField(default='127.0.0.1', help_text='Only accept requests from a IP in this list separated by whitespace . 0.0.0.0 means all.', max_length=2048, verbose_name='From IPs')),
                ('readme_md', models.TextField(blank=True, default='', max_length=4096)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Write API with IP Address Auth',
                'verbose_name_plural': 'Write APIs with IP Address Auth',
                'ordering': ('-creation_date',),
                'get_latest_by': 'creation_date',
            },
        ),
        migrations.CreateModel(
            name='WriteAPIHTTPAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(help_text='The slug is the unique part of the URL for your API.', max_length=100, unique=True)),
                ('http_post', models.BooleanField(blank=True, default=True)),
                ('http_put', models.BooleanField(blank=True, default=True)),
                ('database_name', models.CharField(max_length=100)),
                ('collection_name', models.CharField(max_length=100)),
                ('json_schema', models.TextField(default='{}', help_text='Default "{}", means no JSON Schema.', max_length=20480, verbose_name='JSON Schema')),
                ('readme_md', models.TextField(blank=True, default='', max_length=4096)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='Use ctrl to select multiple groups. If no groups are selected blank, any user may access the API.', related_name='djmongo_write_httpauth_groups', to='auth.Group')),
            ],
            options={
                'verbose_name': 'Write API with HTTPAuth',
                'verbose_name_plural': 'Write APIs with HTTPAuth',
                'ordering': ('-creation_date',),
                'get_latest_by': 'creation_date',
            },
        ),
    ]
