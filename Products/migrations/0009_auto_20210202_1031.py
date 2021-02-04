# Generated by Django 3.1.5 on 2021-02-02 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0008_auto_20210129_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddtoCartModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='category',
            field=models.CharField(choices=[('Fashion', 'Fashion'), ('Health', 'Health'), ('Groceries', 'Groceries'), ('Automobile', 'Automobile')], default='Category', max_length=15, null=True),
        ),
        migrations.DeleteModel(
            name='AddtoCart',
        ),
        migrations.AddField(
            model_name='addtocartmodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='Products.productmodel'),
        ),
    ]
