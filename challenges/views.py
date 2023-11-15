from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
monthly_challenges = {
    "january": "january",
    "february": "february",
    "march": "march",
    "april": "april",
    "may": "may",
    "june": "june",
    "july": "july",
    "august": "august",
    "september": "september",
    "october": "october",
    "november": "november",
    "december": None
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render (request,'challenges/index.html',{
        "months": months
    })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("monthly-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

def monthly_challenges_by_Month(request,month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirected_month = months[month-1]
    redirected_path = reverse("monthly-challenge", args=[redirected_month])
    return HttpResponseRedirect(redirected_path)
    
def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = f"<h3>{challenge_text}</h3>"
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request,"challenges/challenge.html", {"text": challenge_text, "month_name":month})
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data) 
        raise Http404()