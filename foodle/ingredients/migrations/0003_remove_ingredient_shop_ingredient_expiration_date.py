# Generated by Django 4.2.16 on 2024-10-03 13:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0002_alter_ingredient_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='shop',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='expiration_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date de péremption'),
        ),
    ]
