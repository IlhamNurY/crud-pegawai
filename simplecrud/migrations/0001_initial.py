# Generated by Django 2.2.1 on 2019-06-03 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crudsimple',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=50)),
                ('nip', models.IntegerField(max_length=30)),
                ('divisi', models.CharField(max_length=50)),
                ('alamat', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'simplecrud',
            },
        ),
    ]
