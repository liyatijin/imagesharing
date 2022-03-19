from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    file = models.FileField(upload_to='file',default=None)
    description = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    time=models.DateTimeField(auto_now_add=True)
    id = models.AutoField(auto_created=True, primary_key=True,serialize=False,verbose_name='ID')


    
    
    
