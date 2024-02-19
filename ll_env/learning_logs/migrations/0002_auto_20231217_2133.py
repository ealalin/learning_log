# Generated by Django 3.2.18 on 2023-12-17 20:33

from django.db import migrations, models
import django.utils.timezone
import learning_logs.models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='name',
        ),
        migrations.AddField(
            model_name='topic',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=learning_logs.models.TextField(max_length=200),
        ),
    ]
