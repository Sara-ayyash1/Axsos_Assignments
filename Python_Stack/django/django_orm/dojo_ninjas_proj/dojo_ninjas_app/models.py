from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(default="old dojo")
    # Ninjas = reverse lookup via related_name in Ninja model


class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)  #The direct access from Ninja to Dojo
    created_at = models.DateTimeField(auto_now_add=True) # يحفظ الوقت مرة وحدة فقط — لما السجل اتضاف لأول مرة # بعدها ما بيتغير أبداً
    updated_at = models.DateTimeField(auto_now=True) # يحفظ الوقت كل مرة تعمل .save() # بيتحدث تلقائياً دايماً