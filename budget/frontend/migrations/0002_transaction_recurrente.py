# Generated by Django 5.1.4 on 2024-12-14 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='recurrente',
            field=models.BooleanField(default=False, verbose_name='Transaction récurrente'),
        ),
    ]