# Generated by Django 3.2.9 on 2022-01-12 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daihuu', '0020_auto_20220103_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hinh_dai_dien',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
