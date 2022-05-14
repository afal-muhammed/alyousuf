from import_export import resources
from .models import JobOpportunities

class JobResource(resources.ModelResource):
    class Meta:
        model = JobOpportunities
