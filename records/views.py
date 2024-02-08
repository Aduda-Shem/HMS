from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def records(request):


    context = {
    }

    return render(request, 'records/hospital_records.html', context)
