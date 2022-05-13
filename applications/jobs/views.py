import json
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from django.views import View
from applications.jobs.models import JobOpportunities
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import HttpResponseRedirect,HttpResponse
from django.contrib import messages
# Create your views here.


class LandingViewTabular(ListView):
    template_name = 'table-entry.html'
    context_object_name = 'job_listings'
    paginate_by = 8

    def post(self, request):
        #TODO: validate each field . Show appropriate error messages
        title = request.POST.get("job-title", '')
        description = request.POST.get("job-description", '')
        location = request.POST.get("job-location", '')
        company_name = request.POST.get("comapny-name", '')
        contact = request.POST.get("contact", '')
        try:
            JobOpportunities.objects.get_or_create(title=title, job_description=description, location=location,
                                                   company_name=company_name, phone_number=contact)
            data ={}
            data["result"] = "success"
            return HttpResponse(json.dumps(data),
                                content_type="application/json")
        except:
            data = {}
            data["result"] = "Couldnt add job opportunity.Something went wrong"
            return HttpResponse(json.dumps(data),
                                content_type="application/json")


    def get_queryset(self, *args, **kwargs):
        queryset = JobOpportunities.objects.all()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context

# class LandingViewGrid(ListView):
#     template_name = 'job-grid.html'
#     context_object_name = 'job_listings'
#     paginate_by = 8
#
#
#     def get_queryset(self, *args, **kwargs):
#         queryset = JobOpportunities.objects.all()
#         return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context

class ImporterView(View):

    @method_decorator(login_required)
    def get(self, request):
        return render(self.request, 'importer.html')

    def post(self, request):
        rows = request.POST.getlist("table-rows[]", False)
        if request.FILES:
            csv_file = request.FILES["csv_file", False]
            if not csv_file.name.endswith('.csv') and not csv_file.name.endswith('.ods'):
                messages.error(request, 'File is not CSV type')
                return HttpResponseRedirect(reverse("importer"))
                # if file is too large, return
            if csv_file.multiple_chunks():
                messages.error(request, "Uploaded file is too big (%.2f MB)." % (csv_file.size / (1000 * 1000),))
                return HttpResponseRedirect(reverse("importer"))
            data = csv_file.read().decode("utf-8")
            import re
            rows = re.split('\n', data)  # splits along new line
            rows.pop(0)
            rows.pop()
            print(rows)
            for index, row in enumerate(rows):
                cells = row.split(',')
                print(cells)
                job_obj = JobOpportunities()
                job_obj.title = cells[0]
                job_obj.job_description = cells[1]
                job_obj.location = cells[2]
                job_obj.phone_number = cells[3]
                job_obj.company_name = cells[4]
                job_obj.save()
            return redirect('landing')
        elif rows:
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
        else:
            messages.error(request, 'Please copy paste excel data or upload a csv')
            return HttpResponseRedirect(reverse("importer"))
