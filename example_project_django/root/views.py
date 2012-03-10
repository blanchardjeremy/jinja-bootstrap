from django.views.generic.base import TemplateView
from root.forms import LoginForm, RegisterForm
from jingo.helpers import *

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context_data = super(HomeView, self).get_context_data(**kwargs)

        data = {
            'login_form': LoginForm(),
            'register_form': RegisterForm(),
        }

        context_data.update(data)
        return context_data

