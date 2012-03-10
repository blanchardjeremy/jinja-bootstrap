from django.views.generic.base import TemplateView
from root.forms import *
from jingo.helpers import *

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context_data = super(HomeView, self).get_context_data(**kwargs)

        fake_data_to_force_error = {
            'fake_error': '', # required field with no data
        }
        fancy_form = FancyForm(data=fake_data_to_force_error)


        data = {
            'login_form': LoginForm(),
            'inline_form': InlineForm(),
            'register_form': RegisterForm(),
            'fancy_form': fancy_form,
        }



        context_data.update(data)
        return context_data

