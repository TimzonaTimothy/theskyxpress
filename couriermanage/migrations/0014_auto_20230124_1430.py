# Generated by Django 3.0.5 on 2023-01-24 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couriermanage', '0013_auto_20230124_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
