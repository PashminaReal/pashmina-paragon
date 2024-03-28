# Generated by Django 3.2.23 on 2024-03-28 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_full_name', models.CharField(max_length=40)),
                ('user_email', models.EmailField(max_length=50)),
                ('user_contact_number', models.CharField(max_length=11)),
                ('user_address', models.CharField(max_length=60)),
                ('user_postal_code', models.CharField(max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
