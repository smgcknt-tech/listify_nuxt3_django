# Generated by Django 3.2 on 2022-07-19 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20220529_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.item'),
        ),
    ]