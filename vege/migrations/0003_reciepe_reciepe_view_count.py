# Generated by Django 5.0.1 on 2024-03-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_reciepe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reciepe',
            name='reciepe_view_count',
            field=models.IntegerField(default=1),
        ),
    ]
