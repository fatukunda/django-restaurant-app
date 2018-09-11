from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid
"""Model represting a food """
class Food(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular food across the whole restaurant')
    name = models.CharField(max_length=50, blank=False, null=False)
    is_available = models.BooleanField(default = False)

    def __str__(self):
        return self.name

"""Model for representing sauce"""
class Sauce(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular sauce across whole restaurant')
    name = models.CharField(max_length=50, blank=False, null=False, help_text ='Sauce name (e.g Chicken)')
    is_available = models.BooleanField(default = False)

    def __str__(self):
        return self.name
"""Model class for Dessert"""
class Dessert(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular dessert across the whole restaurant')
    name = models.CharField(max_length=100, blank=False, null=False, help_text ='Dessert name (e.g Apple cake)')
    is_available = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class Drink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular drink across whole restaurant')
    name = models.CharField(max_length=50, blank=False, null=False, help_text ='drink name (e.g Cocacola)')
    SOFT_DRINK = 'SD'
    PACKED_JUICE = 'PJC'
    FRESH_JUICE = 'FJC'
    ALCOHOLIC = 'ALC'
    ENERGY_DRINK = 'END'
    drink_categories = (
        (SOFT_DRINK, 'Soft drink'),
        (PACKED_JUICE, 'Packed Juice'),
        (FRESH_JUICE, 'Fresh Juice'),
        (ALCOHOLIC, 'Alcohol'),
        (ENERGY_DRINK, 'Energy drink')
    )
    category = models.CharField(max_length=4, choices = drink_categories, blank=False, null=False)
    is_available = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class DeliveryArea(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular delivery area')
    name = models.CharField(max_length=50, blank=False, null=False, help_text ='Name of the delivery area (e.g Kamwokya)')

    def __str__(self):
        return self.name
class FoodCombination(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular food combination in the whole restaurant')
    foods = models.ManyToManyField(Food, help_text='Select a food to add on this food combination')
    sauces = models.ManyToManyField(Sauce, help_text='Select a sauce to add on this food combination')
    price = models.DecimalField(max_digits=8, decimal_places=2)

class Menu(models.Model):
    food_combinations = models.ManyToManyField(FoodCombination, help_text='Select a food combination to add on the menu')
    drinks = models.ManyToManyField(Drink, help_text='Select a drink to add on the menu')
    desserts = models.ManyToManyField(Dessert, help_text='Select a dessert to add on the menu')

class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular restaurant')
    name = models.CharField(max_length=100, blank=False, null=False, help_text ='Name of the Restaurant (e.g Chop and chop restaurant)')
    info = models.TextField(max_length = 500, blank = False,null=False, help_text='Say something about your restaurant')
    location = models.CharField(max_length=50, blank=False, null=False, help_text='Enter location of your restaurant (e.g Makerere Kikoni')
    is_open = models.BooleanField(default = False)
    email = models.EmailField(max_length=70)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        """Returns the url to access a detail record for this restaurant."""
        return reverse('restaurant-detail', args=[str(self.id)])

"""The order model."""
# class Order(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular order')
#     order_date = 



