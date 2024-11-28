# Generated by Django 5.1.2 on 2024-10-23 23:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_contactform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='custumer_email',
            new_name='customer_email',
        ),
        migrations.AlterField(
            model_name='contactform',
            name='contact_form_uuid',
            field=models.UUIDField(default=uuid.UUID('dc64d813-20fe-4a74-84de-82c530677af8')),
        ),
    ]