# Generated by Django 4.2 on 2023-04-14 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seasonpal', '0018_alter_suggestion_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='produce',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produce', to='seasonpal.produce'),
        ),
        migrations.AlterField(
            model_name='note',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
