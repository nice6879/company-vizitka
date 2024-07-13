from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    director = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

class Hodimlar(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    tel_number = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self) -> str:
        return self.full_name
    

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    

class Murojaat(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    tel_nomer = models.IntegerField()
    murojaat = models.TextField()
    vaqti = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_name