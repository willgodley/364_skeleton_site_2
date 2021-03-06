# Generated by Django 2.1 on 2019-02-07 02:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190118_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular author across whole library', primary_key=True, serialize=False),
        ),
    ]
