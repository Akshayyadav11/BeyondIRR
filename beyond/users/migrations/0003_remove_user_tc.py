# Generated by Django 4.1.2 on 2022-10-12 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_created_at_user_is_active_user_is_admin_user_tc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tc',
        ),
    ]