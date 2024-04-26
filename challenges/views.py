from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    if month == 'january':
        message = "Eat no meat fro entire month January"
    elif month == 'february':
        message = "febraury  challenges are coming up"
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(message)
