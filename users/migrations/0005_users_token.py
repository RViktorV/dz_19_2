# Generated by Django 4.2.2 on 2024-08-14 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_users_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='token',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Токен'),
        ),
    ]
