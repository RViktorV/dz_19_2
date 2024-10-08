# Generated by Django 4.2.2 on 2024-08-14 15:12

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_avatars_users_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Введите номер телефона', max_length=128, null=True, region=None, unique=True, verbose_name='Телефон'),
        ),
    ]
