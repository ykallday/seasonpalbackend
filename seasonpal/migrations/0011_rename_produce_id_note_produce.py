# Generated by Django 4.2 on 2023-04-13 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seasonpal', '0010_rename_produce_note_produce_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='produce_id',
            new_name='produce',
        ),
    ]
