from django.db import models

# Create your models here.
class App(models.Model):
    item = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return str(self.item)

class Post(models.Model):
   post_heading = models.CharField(max_length=200)
   post_text = models.TextField()
   
   def __str__(self):
      return unicode(self.post_heading)

class DataCentre(models.Model):
    MAX_TEMPERATURE = (
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),
        (16, '16'),
        (17, '17'),
        (18, '18'),
        (19, '19'),
        (20, '20'),
        (21, '21'),
        (22, '22'),
        (23, '23'),
        (24, '24'),
        (25, '25'),
        (26, '26'),
        (27, '27'),
        (28, '28'),
        (29, '29'),
        (30, '30'),
        (31, '31'), 
    )
    MIN_TEMPERATURE = (
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),
        (16, '16'),
        (17, '17'),
        (18, '18'),
        (19, '19'),
        (20, '20'),
        (21, '21'),
        (22, '22'),
        (23, '23'),
        (24, '24'),
        (25, '25'),
        (26, '26'),
        (27, '27'),
        (28, '28'),
        (29, '29'),
        (30, '30'),
        (31, '31'), 
    )
    MAX_HUMIDITY = (
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),
        (16, '16'),
        (17, '17'),
        (18, '18'),
        (19, '19'),
        (20, '20'),
        (21, '21'),
        (22, '22'),
        (23, '23'),
        (24, '24'),
        (25, '25'),
        (26, '26'),
        (27, '27'),
        (28, '28'),
        (29, '29'),
        (30, '30'),
        (31, '31'), 
    )
    MIN_HUMIDITY = (
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),
        (16, '16'),
        (17, '17'),
        (18, '18'),
        (19, '19'),
        (20, '20'),
        (21, '21'),
        (22, '22'),
        (23, '23'),
        (24, '24'),
        (25, '25'),
        (26, '26'),
        (27, '27'),
        (28, '28'),
        (29, '29'),
        (30, '30'),
        (31, '31'), 
    )
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    postal_code = models.IntegerField(max_length=6)
    max_temperature = models.FloatField(max_length=2, choices=MAX_TEMPERATURE)
    min_temperature = models.FloatField(max_length=2, choices=MIN_TEMPERATURE)
    max_humidity = models.FloatField(max_length=2, choices=MAX_HUMIDITY)
    min_humidity = models.FloatField(max_length=2, choices=MIN_HUMIDITY)
    time_taken_temp_humid = models.TimeField()
    
    def max_temp(self):
        return self.max_temperature

class Customer(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_number = models.IntegerField(max_length=8)
    home_number = models.IntegerField(max_length=8)
    address = models.CharField(max_length=30)

class IOT_devices(models.Model):
    device = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

class StoreData(models.Model):
    temperature = models.FloatField(max_length=5)
    humidity = models.FloatField(max_length=5)

class Test3(models.Model):
    signal = models.IntegerField()
    payload = models.FloatField()
    EventProcessedUtcTime = models.DateTimeField()
