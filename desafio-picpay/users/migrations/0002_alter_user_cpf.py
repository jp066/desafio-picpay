# Generated by Django 5.1.4 on 2025-01-04 16:13

import users.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, validators=[users.validators.validate_cpf]),
        ),
    ]
