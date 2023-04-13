# Generated by Django 4.2 on 2023-04-13 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seasonpal', '0013_alter_note_produce_alter_note_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='produce',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='seasonpal.produce'),
        ),
        migrations.AlterField(
            model_name='note',
            name='user',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='note', to=settings.AUTH_USER_MODEL),
        ),
    ]