# Generated by Django 4.2.3 on 2023-08-01 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_alter_listing_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]
