from django.shortcuts import render, HttpResponse
from menu.models import Item


def menu_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    # Дополнительная логика для обработки перехода
    return render(request, 'menu/menu_detail.html', {'item': item})


def menu_view(request):
    # return HttpResponse('Menu page')
    return render(request, "menu/index.html")  # в приложении есть templates/menu/menu.html

# from django.views.generic import TemplateView
#
#
# class IndexPageView(TemplateView):
#     template_name = "menu/index.html"

