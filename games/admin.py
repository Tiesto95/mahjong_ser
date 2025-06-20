
from django.contrib import admin
from .models import Category, Game
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display=('name','average_rating','created_at')
    prepopulated_fields={'slug':('title',)}
    filter_horizontal=('categories',)
    fieldsets=((None,{'fields':('name','title','h1','slug','categories','description','image')}),('Game Content',{'fields':('game_code','game_file','is_flash')}),('SEO',{'fields':('meta_title','meta_description','meta_keywords')}),('Stats',{'fields':('views','rating_sum','rating_count')}))
