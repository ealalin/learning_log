# Generated by Django 3.2.18 on 2024-01-05 17:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_entry_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='text',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
