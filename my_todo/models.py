from django.db import models

class List(models.Model):
    item= models.CharField(max_length=200)
    complete= models.BooleanField(default=False)

    def __str__(self):
        self.item +'|'+self.complete
