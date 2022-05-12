from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.views import View
from .models import JobOpportunities
from django.db.models import Q
from django.core.paginator import Paginator
from applications.jobs.models import JobOpportunities
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


class LandingView(ListView):
    template_name = 'table-entry.html'
    context_object_name = 'job_listings'
    paginate_by = 8

    def get_queryset(self, *args, **kwargs):
        queryset = JobOpportunities.objects.all()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context

class ImporterView(View):

    @method_decorator(login_required)
    def get(self, request):
        return render(self.request, 'importer.html')

    def post(self, request):
        rows = request.POST.getlist("table-rows[]")
        for row in rows:
            if row:
                item_list = row.split(",")
                job_obj = JobOpportunities()
                job_obj.title = item_list[0]
                job_obj.job_description = item_list[1]
                job_obj.location = item_list[2]
                job_obj.phone_number = item_list[3]
                job_obj.company_name = item_list[4]
                job_obj.save()
        return redirect("landing")