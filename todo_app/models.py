from django.db import models

# Create your models here
class TodoItems(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    task = models.CharField(max_length=50)
    details = models.CharField(max_length=100,null=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task