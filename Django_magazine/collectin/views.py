from django.shortcuts import render

# Create your views here.
def collections_list(request):
    # Пока передаем пустой контекст, позже сюда добавим данные из БД
    return render(request, 'collectin/index.html')
