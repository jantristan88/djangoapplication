from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Jan Tristan Gaspi', #content placeholders are replaced by 
    }
    return render(request, "index.html", context)

def featureproject(request):
    context ={
        'title': 'Feature Project',
    }
    return render(request, "FeatureProject.html", context)

def publication(request):
    context ={
        'title': 'Publication',
    }
    return render(request, "Publication.html", context)

def github_api_example(request):
    response = requests.get('https://api.github.com/users/jantristan88/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

# def about_me(request):
#     # Django comes with a "shortcut" function called "render", that
#     # lets us read in HTML template files in separate directories to
#     # keep our code better organized.
#     context = {
#         'name': 'Ash Ketchum',
#         'pokemon': 'Pikachu',
#     }
#     return render(request, 'about_me.html', context) #sample: about_me is the one filled up by context


