# Generated by Django 4.2 on 2023-04-14 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seasonpal', '0033_alter_suggestion_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='user',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
