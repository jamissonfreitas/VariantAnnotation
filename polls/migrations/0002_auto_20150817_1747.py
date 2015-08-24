# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vcf',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 17, 17, 47, 57, 425657, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vcf',
            name='file_in',
            field=models.FileField(upload_to=b'', verbose_name=b'VCF in'),
        ),
        migrations.AlterField(
            model_name='vcf',
            name='file_out',
            field=models.FileField(upload_to=b'', verbose_name=b'VCF out'),
        ),
    ]
