from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  client_reference_id = models.CharField(max_length=255, null=True)
  payment_status = models.CharField(max_length=255, null=True)

class Session(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  session_id = models.TextField()
  client_reference_id = models.IntegerField()
  created = models.DateTimeField()
  currency = models.CharField(max_length=255, null=True)
  customer = models.CharField(max_length=255, null=True)
  customer_creation = models.CharField(max_length=255, null=True)
  customer_email = models.CharField(max_length=255, null=True)
  expires_at = models.DateTimeField(max_length=255, null=True)
  livemode = models.BooleanField()
  mode = models.CharField(max_length=255, null=True)
  session_object = models.CharField(max_length=255, null=True)
  payment_intent = models.CharField(max_length=255, null=True)
  payment_link = models.CharField(max_length=255, null=True)
  payment_status = models.CharField(max_length=255, null=True)
  setup_intent = models.CharField(max_length=255, null=True)
  status = models.CharField(max_length=255, null=True)
  submit_type = models.CharField(max_length=255, null=True)
  subscription = models.CharField(max_length=255, null=True)
  success_url = models.TextField(null=True)
  cancel_url = models.TextField(null=True)
  url = models.TextField(null=True)

class CustomerDetails(models.Model):
  customer_details = models.OneToOneField(Session, on_delete=models.CASCADE)
  email = models.CharField(max_length=255, null=True)
  name = models.CharField(max_length=255, null=True)
  phone = models.CharField(max_length=255, null=True)
  tax_exempt = models.CharField(max_length=255, null=True)

class CustomerAddress(models.Model):
  address = models.OneToOneField(CustomerDetails, on_delete=models.CASCADE)
  city = models.CharField(max_length=255, null=True)
  country = models.CharField(max_length=255, null=True)
  line1 = models.CharField(max_length=255, null=True)
  lin2 = models.CharField(max_length=255, null=True)
  postal_code = models.CharField(max_length=255, null=True)
  state = models.CharField(max_length=255, null=True)

