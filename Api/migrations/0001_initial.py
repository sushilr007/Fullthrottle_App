# Generated by Django 3.1 on 2020-08-07 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('User', models.CharField(max_length=50)),
                ('tz', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('user_activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.user')),
            ],
            options={
                'db_table': 'activity_period',
            },
        ),
    ]