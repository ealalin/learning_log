# Generated by Django 4.2.7 on 2023-12-22 06:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_auto_20231217_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
