# Generated by Django 2.2.4 on 2019-11-05 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomIPAuthReadAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_format', models.CharField(choices=[('json', 'JSON'), ('html', 'HTML'), ('csv', 'Comma Separated Value (.csv)')], default='json', max_length=4)),
                ('slug', models.SlugField(help_text='Give your API a unique name', max_length=100)),
                ('query', models.TextField(default='{}', max_length=2048, verbose_name='JSON Query')),
                ('type_mapper', models.TextField(default='{}', max_length=2048, verbose_name='Map non-string variables to numbers or Boolean')),
                ('sort', models.TextField(blank=True, default='', help_text='e.g. [["somefield", 1], ["someotherfield", -1] ]', max_length=2048, verbose_name='Sort Dict')),
                ('return_keys', models.TextField(blank=True, default='', help_text='Default is blank which returns all keys. Separate keys by white space to limitthe keys that are returned.', max_length=2048)),
                ('default_limit', models.IntegerField(default=200, help_text='Limit results to this number unless specified otherwise.')),
                ('from_ip', models.TextField(default='127.0.0.1', help_text='Only accept requests from a IP in this list separated by whitespace . 0.0.0.0 means all.', max_length=2048, verbose_name='From IPs')),
                ('database_name', models.CharField(max_length=100)),
                ('collection_name', models.CharField(max_length=100)),
                ('readme_md', models.TextField(blank=True, default='', max_length=4096)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-creation_date',),
                'get_latest_by': 'creation_date',
            },
        ),
        migrations.CreateModel(
            name='CustomPublicReadAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_format', models.CharField(choices=[('json', 'JSON'), ('html', 'HTML'), ('csv', 'Comma Separated Value (.csv)')], default='json', max_length=4)),
                ('slug', models.SlugField(help_text='Give your API a unique name', max_length=100)),
                ('query', models.TextField(default='{}', max_length=2048, verbose_name='JSON Query')),
                ('type_mapper', models.TextField(default='{}', max_length=2048, verbose_name='Map non-string variables to numbers or Boolean')),
                ('sort', models.TextField(blank=True, default='', help_text='e.g. [["somefield", 1], ["someotherfield", -1] ]', max_length=2048, verbose_name='Sort Dict')),
                ('return_keys', models.TextField(blank=True, default='', help_text='Default is blank which returns all keys. Separate keys by white space to limitthe keys that are returned.', max_length=2048)),
                ('default_limit', models.IntegerField(default=200, help_text='Limit results to this number unless specified otherwise.')),
                ('database_name', models.CharField(max_length=100)),
                ('collection_name', models.CharField(max_length=100)),
                ('readme_md', models.TextField(blank=True, default='', max_length=4096)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-creation_date',),
                'get_latest_by': 'creation_date',
            },
        ),
        migrations.CreateModel(
            name='PublicReadAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('database_name', models.CharField(max_length=256)),
                ('collection_name', models.CharField(max_length=256)),
                ('slug', models.SlugField(help_text='Give your API a unique name', max_length=100)),
                ('search_keys', models.TextField(blank=True, default='', help_text='The default, blank, returns\n                                                all keys. Providing a list of\n                                                keys, separated by whitespace,\n                                                limits the API search to only\n                                                these keys.', max_length=4096)),
                ('readme_md', models.TextField(blank=True, default='', max_length=4096)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'unique_together': {('database_name', 'collection_name', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='OAuth2ReadAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('database_name', models.CharField(max_length=256)),
                ('collection_name', models.CharField(max_length=256)),
                ('slug', models.SlugField(help_text='Give your API a unique name', max_length=100)),
                ('scopes', models.CharField(blank=True, default='*', help_text='Space delimited list of scopes required. * means no scope is required.', max_length=1024)),
                ('search_keys', models.TextField(blank=True, default='', help_text='The default, blank, returns\n                                                all keys. Providing a list of\n                                                keys, separated by whitespace,\n                                                limits the API search to only\n                                                these keys.', max_length=4096)),
                ('readme_md', models.TextField(blank=True, default='', max_length=4096)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'unique_together': {('database_name', 'collection_name', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='IPAuthReadAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('database_name', models.CharField(max_length=256)),
                ('collection_name', models.CharField(max_length=256)),
                ('slug', models.SlugField(help_text='Give your API a unique name', max_length=100)),
                ('from_ip', models.TextField(default='127.0.0.1', help_text='Only accept requests from a IP in this list separated by whitespace . 0.0.0.0 means all.', max_length=2048, verbose_name='From IPs')),
                ('search_keys', models.TextField(blank=True, default='', help_text='The default, blank, returns\n                                                all keys. Providing a list of\n                                                keys, separated by whitespace,\n                                                limits the API search to only\n                                                these keys.', max_length=4096)),
                ('readme_md', models.TextField(blank=True, default='', max_length=4096)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'unique_together': {('database_name', 'collection_name', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='CustomOAuth2ReadAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_format', models.CharField(choices=[('json', 'JSON'), ('html', 'HTML'), ('csv', 'Comma Separated Value (.csv)')], default='json', max_length=4)),
                ('slug', models.SlugField(help_text='Give your API a unique name', max_length=100)),
                ('scopes', models.CharField(blank=True, default='*', help_text='Space delimited list of scopes required. * means no scope is required.', max_length=1024)),
                ('query', models.TextField(default='{}', max_length=2048, verbose_name='JSON Query')),
                ('type_mapper', models.TextField(default='{}', max_length=2048, verbose_name='Map non-string variables to numbers or Boolean')),
                ('sort', models.TextField(blank=True, default='', help_text='e.g. [["somefield", 1], ["someotherfield", -1] ]', max_length=2048, verbose_name='Sort Dict')),
                ('return_keys', models.TextField(blank=True, default='', help_text='Default is blank which returns all keys. Separate keys by white space to limitthe keys that are returned.', max_length=2048)),
                ('default_limit', models.IntegerField(default=200, help_text='Limit results to this number unless specified otherwise.')),
                ('database_name', models.CharField(max_length=100)),
                ('collection_name', models.CharField(max_length=100)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('readme_md', models.TextField(blank=True, default='', max_length=4096)),
            ],
            options={
                'ordering': ('-creation_date',),
                'get_latest_by': 'creation_date',
                'unique_together': {('database_name', 'collection_name', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='CustomHTTPAuthReadAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_format', models.CharField(choices=[('json', 'JSON'), ('html', 'HTML'), ('csv', 'Comma Separated Value (.csv)')], default='json', max_length=4)),
                ('slug', models.SlugField(help_text='Give your API a unique name', max_length=100)),
                ('query', models.TextField(default='{}', max_length=2048, verbose_name='JSON Query')),
                ('type_mapper', models.TextField(default='{}', max_length=2048, verbose_name='Map non-string variables to numbers or Boolean')),
                ('sort', models.TextField(blank=True, default='', help_text='e.g. [["somefield", 1], ["someotherfield", -1] ]', max_length=2048, verbose_name='Sort Dict')),
                ('return_keys', models.TextField(blank=True, default='', help_text='Default is blank which returns all keys. Separate keys by white space to limitthe keys that are returned.', max_length=2048)),
                ('default_limit', models.IntegerField(default=200, help_text='Limit results to this number unless specified otherwise.')),
                ('database_name', models.CharField(max_length=100)),
                ('collection_name', models.CharField(max_length=100)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('readme_md', models.TextField(blank=True, default='', max_length=4096)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'ordering': ('-creation_date',),
                'get_latest_by': 'creation_date',
            },
        ),
        migrations.CreateModel(
            name='HTTPAuthReadAPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('database_name', models.CharField(max_length=256)),
                ('collection_name', models.CharField(max_length=256)),
                ('slug', models.SlugField(help_text='Give your API a unique name', max_length=100)),
                ('search_keys', models.TextField(blank=True, default='', help_text='The default, blank, returns\n                                                all keys. Providing a list of\n                                                keys, separated by whitespace,\n                                                limits the API search to only\n                                                these keys.', max_length=4096)),
                ('readme_md', models.TextField(blank=True, default='', max_length=4096)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='djmongo_http_auth_read_api', to='auth.Group')),
            ],
            options={
                'unique_together': {('database_name', 'collection_name', 'slug')},
            },
        ),
    ]
