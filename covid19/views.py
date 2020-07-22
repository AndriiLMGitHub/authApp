from django.shortcuts import render
from covid import Covid
# Create your views here.

def covid19(request):
    covid = Covid()
    context = {
        'get_total_active_cases' : covid.get_total_active_cases(),
        'get_total_deaths' : covid.get_total_deaths(),
        'get_total_confirmed_cases' : covid.get_total_confirmed_cases(),
        'get_all_data': covid.get_data(),
        'get_total_recovered' : covid.get_total_recovered(),
        'list_countries' : covid.list_countries(),
        'ukraine_cases' : covid.get_status_by_country_name("ukraine")
    }
    return render(request, 'covid19/covid19.html', context)
