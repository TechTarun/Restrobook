# Generated by Django 2.2.6 on 2019-12-29 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20191228_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_item', models.CharField(max_length=20)),
                ('item_qty', models.CharField(max_length=4)),
                ('item_num', models.IntegerField()),
                ('item_price', models.IntegerField()),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Customer')),
            ],
        ),
    ]
