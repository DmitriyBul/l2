from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Bb
from .models import Rubric
from django.views.generic.edit import CreateView
from .forms import BbForm
from django.urls import reverse_lazy
# Create your views here.


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'builds/index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'builds/by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = 'builds/create.html'
    form_class = BbForm
    success_url = '/builds/'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
