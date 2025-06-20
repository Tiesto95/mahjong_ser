
from django.db import models
class Category(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)
    description=models.TextField()
    def __str__(self): return self.name

class Game(models.Model):
    name=models.CharField(max_length=120)
    title=models.CharField(max_length=255)
    h1=models.CharField(max_length=255,null=True,blank=True)
    slug=models.SlugField(unique=True)
    categories=models.ManyToManyField(Category,related_name='games')
    description=models.TextField()           # HTML allowed
    image=models.ImageField(upload_to='game_covers/',null=True,blank=True)
    game_file=models.FileField(upload_to='games/',null=True,blank=True)
    game_code=models.TextField(null=True,blank=True)
    is_flash=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    meta_title=models.CharField(max_length=255,null=True,blank=True)
    meta_description=models.TextField(null=True,blank=True)
    meta_keywords=models.CharField(max_length=255,null=True,blank=True)
    views=models.PositiveIntegerField(default=0)
    rating_sum=models.PositiveIntegerField(default=0)
    rating_count=models.PositiveIntegerField(default=0)
    rated_ips=models.TextField(default='',blank=True)
    def average_rating(self):
        return round(self.rating_sum/self.rating_count,1) if self.rating_count else 0
    def has_rated(self,ip):
        return ip in self.rated_ips.split(',')
    def save_rating_ip(self,ip):
        if ip and not self.has_rated(ip):
            self.rated_ips+=(f'{ip},' if self.rated_ips else ip)
    def __str__(self): return self.title
