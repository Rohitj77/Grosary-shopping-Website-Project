# Generated by Django 4.1.1 on 2022-10-29 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_food_data', '0006_alter_shop_food_title_alter_shop_main_food'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='main_food',
        ),
    ]
