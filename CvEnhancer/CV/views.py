from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Experience, Skill, Rate
from django.template import loader
import json
from django.views.decorators.csrf import csrf_exempt


def index(request):
    rating_list = Rate.objects.all()
    template = loader.get_template("CV/index.html")
    context = {
        "rating_list": rating_list,
    }
    return HttpResponse(template.render(context, request))

def form_page(request):
    experience_list = list(Experience.objects.values())
    skill_list = list(Skill.objects.values())
    context = {
        "experience_list":json.dumps(experience_list),
        "skill_list":json.dumps(skill_list)
    }
    return render(request, 'CV/form.html',context)

def about_us_page(request):
    rating_list = Rate.objects.all()
    template = loader.get_template('CV/aboutus.html')
    context = {
        "rating_list": rating_list,
    }
    return HttpResponse(template.render(context, request))
    

def rate_page(request):
    rating_list = Rate.objects.all()
    template = loader.get_template('CV/rate.html')
    context = {
        "rating_list": rating_list,
    }
    return HttpResponse(template.render(context, request))

def rate_site(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        rating_val = request.POST.get('rating_val')
        comment = request.POST.get('comment')
        rating = Rate(rating=rating, rating_val=rating_val,comment=comment)
        rating.save()
    ratinglast = Rate.objects.last()
    rating_list = Rate.objects.all()
    template = loader.get_template("CV/thankforrating.html")
    context = {
        "ratinglast": ratinglast,
        "rating_list":rating_list
    }
    return HttpResponse(template.render(context, request))
