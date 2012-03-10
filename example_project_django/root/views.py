from django.views.generic.base import TemplateView
from bootstrap.views import FOOCAR


class HomeView(TemplateView):
    template_name = 'home.html'
    a = FOOCAR
    pass