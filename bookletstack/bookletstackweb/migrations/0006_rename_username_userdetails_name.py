# Generated by Django 4.0.3 on 2023-06-05 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookletstackweb', '0005_userdetails_user_alter_userdetails_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='username',
            new_name='name',
        ),
    ]
