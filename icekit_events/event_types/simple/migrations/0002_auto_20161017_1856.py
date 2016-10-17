# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icekit_event_types_simple', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='simpleevent',
            options={'verbose_name': 'Simple event'},
        ),
        migrations.AlterField(
            model_name='simpleevent',
            name='eventbase_ptr',
            field=models.OneToOneField(to='icekit_events.EventBase', auto_created=True, serialize=False, parent_link=True, primary_key=True),
        ),
    ]
