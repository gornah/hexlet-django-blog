from django.shortcuts import render
from django.views.generic.base import TemplateView


# def index(request):
#    return render(request, 'index.html', context={
#        'who': 'World'
#        })
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'Hexlet Django Blog'
        return context


def base(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'about.html')
