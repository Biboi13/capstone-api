# Generated by Django 2.1.11 on 2020-06-14 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VCT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vct_name', models.CharField(max_length=200)),
                ('vct_active_users', models.CharField(max_length=200)),
                ('vct_developer', models.CharField(max_length=200)),
            ],
        ),
    ]
