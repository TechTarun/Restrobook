# Generated by Django 2.2.6 on 2019-12-28 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_num', models.IntegerField(max_length=2)),
                ('phone_num', models.IntegerField(max_length=10)),
                ('cart_value', models.IntegerField(max_length=3)),
            ],
        ),
    ]
