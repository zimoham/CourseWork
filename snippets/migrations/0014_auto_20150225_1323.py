# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0013_episode_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='season',
        ),
        migrations.DeleteModel(
            name='Episode',
        ),
        migrations.RemoveField(
            model_name='season',
            name='serial',
        ),
        migrations.DeleteModel(
            name='Season',
        ),
    ]
