from django.db import models

class Blog(models.Model):
    title=models.TextField(max_length=100)
    pub_date=models.DateTimeField()
    body=models.TextField()
    img=models.ImageField(upload_to='images')
