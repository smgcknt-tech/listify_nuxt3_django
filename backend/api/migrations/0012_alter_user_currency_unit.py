# Generated by Django 3.2 on 2022-03-01 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20220301_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currency_unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.currency_unit'),
        ),
    ]