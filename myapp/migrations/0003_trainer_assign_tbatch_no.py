# Generated by Django 2.2 on 2022-06-21 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20220618_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer_assign',
            name='tbatch_no',
            field=models.IntegerField(default=None),
        ),
    ]
