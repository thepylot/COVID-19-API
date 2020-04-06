# Generated by Django 3.0.5 on 2020-04-06 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coronavirus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('cases', models.IntegerField()),
                ('death', models.IntegerField()),
                ('recovers', models.IntegerField()),
            ],
        ),
    ]