
from django.contrib import admin
from .models import Category, Game, Menu
from django.utils.safestring import mark_safe

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    # колонки в списке категорий
    list_display       = ('name', 'slug', 'title', 'alt', 'link_text')
    search_fields      = ('name', 'title', 'alt')
    prepopulated_fields = {'slug': ('name',)}

    # группы полей на форме добавления/редактирования
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'title', 'alt', 'link_text')
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # колонки в списке категорий
    list_display       = ('name', 'slug', 'title', 'h1', 'short_text')
    search_fields      = ('name', 'title', 'h1')
    prepopulated_fields = {'slug': ('name',)}

    # группы полей на форме добавления/редактирования
    fieldsets = (
        (None, {
            'fields': ('name', 'slug')
        }),
        ('SEO', {
            'fields': ('title', 'h1', 'description')
        }),
        ('Полный текст', {
            'fields': ('text',),
            'classes': ('collapse',),       # сворачиваемый блок — по желанию
        }),
    )

    # показываем первые 50 симв. текста в списке
    def short_text(self, obj):
        return mark_safe(obj.text[:50] + '…') if obj.text else '—'
    short_text.short_description = 'Текст'
    
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # показ в списке ‒ добавили type_game
    list_display = ('name', 'type_game', 'average_rating', 'created_at')

    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('categories',)

    fieldsets = (
        (None, {
            # добавили type_game в блок основных полей
            'fields': ('name', 'type_game', 'title', 'h1', 'slug',
                       'categories', 'description', 'image')
        }),
        ('Game Content', {
            'fields': ('game_code', 'game_file', 'is_flash')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Stats', {
            'fields': ('views', 'rating_sum', 'rating_count')
        }),
    )