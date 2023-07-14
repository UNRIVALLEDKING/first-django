from django.db import models

# Create your models here.


# Creating a model called "Product" that represents a database table
class Product(models.Model):
    # Defining fields for the "Product" model

    # A character field for the title of the product with a maximum length of 120 characters
    title = models.CharField(max_length=120)

    # A text field for the content or description of the product, which can be blank (optional) and can have null values in the database
    content = models.TextField(blank=True, null=True)

    # A decimal field for the price of the product with a maximum of 15 digits and 2 decimal places. It has a default value of 99.99.
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return "202"
