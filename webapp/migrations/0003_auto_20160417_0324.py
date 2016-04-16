# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_organ_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='enrollmentDate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='prevKidneyDonor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='reactiveAntibodies',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='organ',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
