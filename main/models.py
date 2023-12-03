from django.db import models


class baseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Product_mst(baseModel):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.product_name

class Product_sub_cat(baseModel):
    product = models.OneToOneField(Product_mst, on_delete=models.CASCADE, related_name='productsubcat')
    product_price = models.DecimalField(max_digits=100, decimal_places=2)
    product_image = models.ImageField(upload_to='product_images/')
    product_model = models.CharField(max_length=255)
    product_ram = models.CharField(max_length=255)

    def __str__(self):
        return self.product.product_name