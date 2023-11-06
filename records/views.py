from django.shortcuts import render

# Create your views here.
def records(request):


    context = {
    }

    return render(request, 'records/hospital_records.html', context)
