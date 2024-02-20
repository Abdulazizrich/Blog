from django.shortcuts import render
from mainApp.models import *
from django.views import View


class Home(View):
    def get(self, request):
        return render(request, 'home.html')


class About(View):
    def get(self, request):
        return render(request, 'about.html')


class Blog(View):
    def get(self, request):
        months_dict = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
                       '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November',
                       '12': 'December'}
        years = []
        months = []
        articles = Article.objects.all()
        for i in articles:
            years.append(str(i.date)[:4])
            months.append(str(i.date)[:4]+months_dict[str(i.date)[5:7]])

        context = {
            'years': years,
            'months':months,
            'articles': articles,
        }
        return render(request, 'blog.html', context)
