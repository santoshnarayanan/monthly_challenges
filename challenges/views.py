from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

monthly_challenges_data ={
    "january": "Eat no meat fro entire month January",
    "february": "febraury  challenges are coming up",
    "march": "Learn Django for life",
    "april": "Do excercise for entire month April",
    "may": "Learn Flask from scratch",
    "june": "Its rainfall time",
    "july": "Learn FastAPi from scratch",
    "august": "Learn AWS from scratch",
    "september": "Autum time",
    "october": "Winter frost",
    "november": "Learn Azure from scratch",
    "december": "Coldest month of the year",
}
# Create your views here.


def monthly_challenge_number(request, month):
    months = list(monthly_challenges_data.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month -1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #/challenge/jaunary
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        message = monthly_challenges_data[month]
    except:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(message)
