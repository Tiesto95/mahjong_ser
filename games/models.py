
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255, verbose_name='Title')
    alt = models.CharField(max_length=255, verbose_name='Alt')
    link_text = models.CharField(max_length=255, verbose_name='Текст ссылки')

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255, verbose_name='Title', blank=True)
    h1 = models.CharField(max_length=255, verbose_name='H1', blank=True)
    text = models.TextField(verbose_name='Текст (HTML без экранирования)', blank=True)
    description = models.TextField(verbose_name='Краткое описание', blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Game(models.Model):
    class TypeGame(models.TextChoices):
        HTML5   = "HTML5",   "HTML5"
        FLASH   = "Flash",   "Flash"

    name=models.CharField(max_length=120)
    title=models.CharField(max_length=255)
    h1=models.CharField(max_length=255,null=True,blank=True)
    slug=models.SlugField(unique=True)
    categories=models.ManyToManyField(Category,related_name='games')
    description=models.TextField()           # HTML allowed
    image=models.ImageField(upload_to='game_covers/',null=True,blank=True)
    game_file=models.FileField(upload_to='games/',null=True,blank=True)
    game_code=models.TextField(null=True,blank=True)
    type_game = models.CharField(max_length=40,
        choices=TypeGame.choices,
        default=TypeGame.HTML5,)
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
