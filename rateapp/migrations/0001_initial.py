# Generated by Django 3.1.2 on 2021-05-06 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ident', models.CharField(max_length=3)),
                ('rate', models.IntegerField()),
                ('time_point', models.DateTimeField()),
            ],
        ),
    ]
