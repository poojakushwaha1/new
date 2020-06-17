# Generated by Django 3.0.7 on 2020-06-16 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=40)),
                ('salary', models.IntegerField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]
