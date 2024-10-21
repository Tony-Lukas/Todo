from django.db import models

class TodoGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# Create your models here
class TodoItem(models.Model):
    group = models.ForeignKey(TodoGroup,on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    task = models.CharField(max_length=50)
    details = models.CharField(max_length=100,null=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task