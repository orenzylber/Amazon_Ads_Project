from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    # Add any other fields relevant to the admin accounts
    
    def __str__(self):
        return self.username

class CustomerAccount(models.Model):
    name = models.CharField(max_length=100)
    # Add any other fields relevant to the customer accounts
    
    def __str__(self):
        return self.name

class Campaign(models.Model):
    customer_account = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # Add any other fields relevant to the campaigns
    
    def __str__(self):
        return self.name

class APIKey(models.Model):
    admin = models.OneToOneField(Admin, on_delete=models.CASCADE)
    access_key = models.CharField(max_length=100)
    secret_key = models.CharField(max_length=100)
    # Add any other fields relevant to the API keys
    
    def __str__(self):
        return f"API Key for {self.admin.username}"
# Create your models here.
