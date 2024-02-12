from django.shortcuts import render, HttpResponse


def menu_view(request):
    # return HttpResponse('Menu page')
    return render(request, "menu/index.html")  # в приложении есть templates/menu/menu.html

# from django.views.generic import TemplateView
#
#
# class IndexPageView(TemplateView):
#     template_name = "menu/index.html"

