# Generated by Django 5.1.2 on 2024-11-29 23:49

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_flan_options_flan_is_premium_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='contact_form_uuid',
            field=models.UUIDField(default=uuid.UUID('d20aa13f-92a9-42e5-bb34-86b24d87771b')),
        ),
    ]
