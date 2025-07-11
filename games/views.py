
from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import Category,Game,Menu

def _ip(request):
    x=request.META.get('HTTP_X_FORWARDED_FOR')
    return x.split(',')[0].strip() if x else request.META.get('REMOTE_ADDR')

def index(r):
    c=get_object_or_404(Category,slug='index_page')
    return render(r,'index.html',{'page':c, 'menus':Menu.objects.all(), 'games':Game.objects.all()})

def category_detail(r,slug):
    c=get_object_or_404(Category,slug=slug)
    return render(r,'category.html',{'category':c,'menus':Menu.objects.all(),'games':c.games.all()})

def game_detail(r,slug):
    g=get_object_or_404(Game,slug=slug)
    key=f'v{g.id}'
    if not r.session.get(key):
        g.views+=1;g.save();r.session[key]=True
    related=Game.objects.filter(categories__in=g.categories.all()).exclude(id=g.id).distinct()[:8]
    return render(r,'game_detail.html',{'game':g, 'menus':Menu.objects.all(),'related_games':related})

def rate_game(r,slug):
    if r.method=='POST':
        g=get_object_or_404(Game,slug=slug)
        rating=int(r.POST.get('rating',0))
        ip=_ip(r)
        if 1<=rating<=5 and not g.has_rated(ip):
            g.rating_sum+=rating;g.rating_count+=1;g.save_rating_ip(ip);g.save()
            return JsonResponse({'success':True,'average':g.average_rating()})
        return JsonResponse({'success':False,'reason':'Already rated'})
    return JsonResponse({'success':False})
