# Generated by Django 4.2 on 2023-04-13 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seasonpal', '0016_alter_note_produce_alter_note_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
