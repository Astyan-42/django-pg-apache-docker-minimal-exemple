from django.db import models

# Create your models here.

class ExempleDB(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255, unique=True, db_index=True)
    
    def __str__(self):
        return self.name



