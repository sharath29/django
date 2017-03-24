from django.shortcuts import render
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "game/game.html"

def index(request):
    return render(request, 'game/index.html')

