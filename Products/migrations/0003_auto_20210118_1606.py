# Generated by Django 3.1.5 on 2021-01-18 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_addtocart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
