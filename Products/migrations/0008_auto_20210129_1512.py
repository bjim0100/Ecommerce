# Generated by Django 3.1.5 on 2021-01-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_auto_20210127_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='category',
            field=models.CharField(choices=[('Automobile', 'Automobile'), ('Fashion', 'Fashion'), ('Health', 'Health'), ('Groceries', 'Groceries')], default='Category', max_length=15, null=True),
        ),
    ]
