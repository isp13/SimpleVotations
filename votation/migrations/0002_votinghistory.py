# Generated by Django 2.0.6 on 2019-02-09 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotingHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('golosid', models.IntegerField()),
                ('userid', models.IntegerField()),
                ('date', models.DateTimeField(null=True)),
            ],
        ),
    ]
