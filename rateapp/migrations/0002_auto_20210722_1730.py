# Generated by Django 3.1.2 on 2021-07-22 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rateapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254)),
                ('key', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('role', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='rate',
            name='time_point',
            field=models.DateTimeField(db_index=True),
        ),
    ]
