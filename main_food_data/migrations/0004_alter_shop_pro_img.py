# Generated by Django 4.1.1 on 2022-10-29 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_food_data', '0003_alter_shop_waight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='pro_img',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='media/'),
        ),
    ]
