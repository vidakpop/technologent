from django.db import models

#categories of products
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name  #returns the name in admin
    
    class Meta:
        verbose_name_plural='categories'


# customers
class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#all of our products
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(default=0,decimal_places=2,max_digits=8)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=10000,default='',blank=True,null=True)
    image=models.ImageField(upload_to='uploads/product/')

    #add sale 
    on_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField(default=0,decimal_places=2,max_digits=8)

    def __str__(self):
        return self.name
    