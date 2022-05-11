from django.shortcuts import render
from django.views.generic import ListView
from .models import JobOpportunities
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


class LandingView(ListView):
    template_name = 'table-entry.html'
    context_object_name = 'categories'
    paginate_by = 8

    def get_queryset(self, *args, **kwargs):
        # query_string = self.request.GET.get('categorySearch', '')
        queryset = JobOpportunities.objects.all()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        categories = self.get_queryset()
        paginator = Paginator(categories, self.paginate_by)
        page = self.request.GET.get('page', 1)
        context['categories'] = paginator.page(page)
        return context

class ImporterView(ListView):
    template_name = 'landing.html'
    context_object_name = 'categories'
    paginate_by = 8

    def get_queryset(self, *args, **kwargs):
        # query_string = self.request.GET.get('categorySearch', '')
        queryset = JobOpportunities.objects.all()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        categories = self.get_queryset()
        paginator = Paginator(categories, self.paginate_by)
        page = self.request.GET.get('page', 1)
        context['categories'] = paginator.page(page)
        return context

