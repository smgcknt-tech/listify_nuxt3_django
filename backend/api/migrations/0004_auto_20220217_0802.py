# Generated by Django 3.2 on 2022-02-16 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220216_0800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='meal_plan_id',
            new_name='meal_plan',
        ),
        migrations.RenameField(
            model_name='meal',
            old_name='meal_type_id',
            new_name='meal_type',
        ),
        migrations.RenameField(
            model_name='meal',
            old_name='menu_id',
            new_name='menu',
        ),
        migrations.RenameField(
            model_name='menu_item',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='menu_item',
            old_name='measurement_unit_id',
            new_name='measurement_unit',
        ),
        migrations.RenameField(
            model_name='menu_item',
            old_name='menu_id',
            new_name='menu',
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('currency_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.currency_unit')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='list',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.AddField(
            model_name='menu',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
    ]