# Generated by Django 3.0.5 on 2023-04-30 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couriermanage', '0024_auto_20230429_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier',
            name='tracking_id',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
