from django.db import models


class Client(models.Model):
    gln_client = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class Branch(models.Model):
    gln_branch = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"


class Product(models.Model):
    gtin_producto = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Inventory(models.Model):
    DateTimeField = models.DateTimeField(auto_now=True)
    gln_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    gln_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    gtin_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    final_count = models.IntegerField(default=0)
    price_unity = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventories"
