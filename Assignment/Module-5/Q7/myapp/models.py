from django.db import models

# Create your models here.

class product_master(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.product_name

class sub_category(models.Model):
    product_name=models.ForeignKey(product_master,on_delete=models.CASCADE)
    product_price=models.IntegerField()
    product_img=models.ImageField(upload_to='images')
    product_model=models.CharField(max_length=100)
    product_ram=models.IntegerField()

    def __str__(self) -> str:
        return self.product_name.product_name