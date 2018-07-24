from django.shortcuts import render
from .models import Job
# Create your views here. HERE IS JOBS
def home(request):

    jobs = Job.objects

    return render(request, 'jobs/index.html', {'jobs': jobs})