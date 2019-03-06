import requests
import glob #finds pathnames matching a specified pattern
import os #extracts useful parts of file paths
from django.http import HttpResponse
from django.shortcuts import render

def content_files():
    all_html_files = glob.glob("templates/*.html") #looks for a list of files w/ a pattern, .html
    pages = [] #builds from the contents of the tempates directory = content/*.html
    for html_file in all_html_files:
        file_path = html_file
        file_name = os.path.basename(file_path) #os in effect for file path extraction
        name_only, extension = os.path.splitext(file_name)

        pages.append({ #refactored version
            "filename": 'content/' + name_only + extension,
            "title": name_only,
            "output": 'docs/' + name_only + extension,
            "links": name_only + extension,
        })
    return pages


def index(request):
    content_html = open("content/content.html").read()
    context = {
        "content": content_html, #content placeholders are replaced by 
    }
    return render(request, "base.html", context)

def featureproject(request):
    context ={
        "content":
    }
    return render(request, "FeatureProject.html", context)

def publication(request):
    content ={
        "content":
    }
    return render(request, "Publication.html", context)

def github_api_example(request):
    # We can also combine Django with APIs
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


