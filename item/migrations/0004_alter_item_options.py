# Generated by Django 4.2.6 on 2023-10-29 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_alter_category_options_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',), 'verbose_name_plural': 'Items'},
        ),
    ]
