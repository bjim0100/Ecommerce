from django.db import models


class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    image1 = models.ImageField(blank=True, upload_to='images')
    image2 = models.ImageField(blank=True, upload_to='images')
    image3 = models.ImageField(blank=True, upload_to='images')
    date = models.DateTimeField(null=True, auto_now=True)
    status = {
        ('Fashion', 'Fashion'),
        ('Automobile', 'Automobile'),
        ('Groceries', 'Groceries'),
        ('Health', 'Health')
    }

    category = models.CharField(max_length=15, choices=status, default='Category', null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date']


class AddtoCartModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE,related_name='product')
    quantity = models.PositiveIntegerField(default = 1)



