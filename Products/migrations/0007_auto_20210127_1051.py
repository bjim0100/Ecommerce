# Generated by Django 3.1.5 on 2021-01-27 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_auto_20210127_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='category',
            field=models.CharField(choices=[('Groceries', 'Groceries'), ('Automobile', 'Automobile'), ('Health', 'Health'), ('Fashion', 'Fashion')], default='Category', max_length=15, null=True),
        ),
    ]