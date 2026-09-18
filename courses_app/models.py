from django.db import models



class Course(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()
    situation = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    image = models.ImageField(null=True,upload_to='test')

    def __str__(self):
        return f"{self.title} - {self.description[:30]}"