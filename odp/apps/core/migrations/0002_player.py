# Generated by Django 2.2.6 on 2019-10-29 12:06

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id',
                 models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                  verbose_name='ID')),
                ('team_id', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number',
                 phonenumber_field.modelfields.PhoneNumberField(max_length=128,
                                                                region=None)),
                ('full_name', models.CharField(max_length=200)),
                ('open_dota_account_id', models.IntegerField()),
                ('solo_competive_rank', models.IntegerField()),
                ('competive_rank', models.IntegerField()),
                ('rank_tier', models.IntegerField()),
                ('leaderboard_rank', models.IntegerField()),
                ('steamid', models.CharField(max_length=100)),
                ('avatar', models.URLField(max_length=500)),
                ('loccountrycode', models.CharField(max_length=5)),
            ],
        ),
    ]
