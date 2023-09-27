# Generated by Django 4.2.5 on 2023-09-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('cashback_point', models.IntegerField(default=0)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now=True)),
                ('is_mailing_required', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]