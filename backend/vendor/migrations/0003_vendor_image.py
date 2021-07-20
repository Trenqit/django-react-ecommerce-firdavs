# Generated by Django 3.2.3 on 2021-07-18 15:13

from django.db import migrations
import vendor.models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_friend'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, help_text='Upload a profile image', null=True, upload_to=vendor.models.upload_path, verbose_name='Image'),
        ),
    ]