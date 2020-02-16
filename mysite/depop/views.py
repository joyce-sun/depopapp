from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import json
import pprint
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from depop.templates.forms import HomeForm


# def homepage(request):
#     # return HttpResponse('homepage')
#     name = uname
#     followers = display_count(uname)
#     return render(request, 'homepage.html', {'username': name}, {'follower_count': followers})

# Create your views here.

class HomeView(TemplateView):
    template_name = 'homepage.html'

    def get(self, request):
        form = HomeForm()
        return render(Request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']

        args = {'form': form, 'text': text}
        return render(Request, self.template_name, args)



def index(request, uname="depop"):
    # assume ing we have a template
    # we just say
    # the template will have a variable for followers,
    # and we just pass it that. the template will be defined somewhere else
    # return renderTemplate(display_count(uname))
    name = uname
    followers = display_count(uname)
    return render(request, 'homepage.html', {'username': name, 'follower_count': followers})
    # return HttpResponse("Hello, world. " + uname + " has " + display_count(uname) + " followers.")


def display_count(u_name):
    URL = 'https://www.depop.com/' + u_name + "/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='__NEXT_DATA__')
    d = json.loads(results.text)
    try:
        follower_count = d['props']['pageProps']['shop']['followers']
        return str(follower_count)
    except KeyError:
        return "invalid username"