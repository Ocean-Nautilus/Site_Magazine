from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def favorites(request):
    return render(request, 'core/favorites.html')

def catalog(request):
    return render(request, 'catalog/catalog.html')

def collections_list(request):
    # Пока передаем пустой контекст, позже сюда добавим данные из БД
    return render(request, 'collectin/index.html')

def product_detail(request):
    return render(request, 'core/product_detail.html')

def cart(request):
    return render(request, 'cart/cart.html')

def profile(request):
    return render(request, 'core/profile.html')