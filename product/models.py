from django.db import models
from django.shortcuts import redirect
from django.urls import reverse


class Catagory(models.Model):
    name = models.CharField(max_length=200)
    slug= models.SlugField(max_length=200,unique=True)
    image = models.ImageField(upload_to='category')

    class Meta:
        ordering= ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        
    def __str__(self):
        return self.name
    



class Product(models.Model):
    category = models.ForeignKey(Catagory,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['id','slug'])
        ]
    def __str__(self) -> str:
        return f'{self.name} by {self.category}'
    
    def get_absolute_url(self):
        return reverse('product_detail',args=[self.id,self.slug])
    
class Review(models.Model):
    review = models.TextField()
    emial = models.EmailField()
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_review')
    

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['name'])
        ]
    def __str__(self):
        return f'review by {self.name} for {self.product}'