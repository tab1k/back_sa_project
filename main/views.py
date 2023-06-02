from django.views import View
from django.shortcuts import render


class HomeView(View):

    def get(self, request):
        # Логика обработки GET-запроса
        return render(request, 'main/main.html')

    def post(self, request):
        # Логика обработки POST-запроса
        # ...
        return render(request, 'main/result.html')


class AboutView(View):

    def get(self, request):
        return render(request, 'main/about_us.html')

    def post(self, request):
        # Логика обработки POST-запроса
        # ...
        return render(request, 'result.html')

