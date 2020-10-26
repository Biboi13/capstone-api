# Generated by Django 2.1.11 on 2020-06-18 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200615_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respondance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_name', models.CharField(max_length=200)),
                ('res_place', models.CharField(max_length=200)),
                ('res_internet_bandwidth', models.CharField(max_length=200)),
                ('res_satifactory', models.CharField(max_length=200)),
                ('res_started_using_vct_name', models.DateField(verbose_name='date published')),
                ('res_recommend_vct', models.CharField(max_length=200)),
                ('res_type', models.CharField(max_length=200)),
                ('res_problem_occurred', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Prob_occur')),
            ],
        ),
        migrations.RemoveField(
            model_name='individual',
            name='indv_problem_occurred',
        ),
        migrations.RemoveField(
            model_name='individual',
            name='indv_used_vct',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='org_problem_occurred',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='org_used_vct',
        ),
        migrations.AlterField(
            model_name='vct',
            name='vct_active_users',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Individual',
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
        migrations.AddField(
            model_name='respondance',
            name='res_used_vct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.VCT'),
        ),
    ]
