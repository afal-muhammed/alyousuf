# Generated by Django 3.2 on 2022-05-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobopportunities',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]