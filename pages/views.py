from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
# View is where we create all sort of things for pages. Vies handle various webpages
# We can have clases and functions

# custom name for homepage. add a _view for convention
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user, " le request")
    # return an html template or document add templates directory in settings
    return render(request, "home.html", {})
    # return HttpResponse("<h1>Hello World This is Homepage</h1>") #String of html code, but has nothing to do with django.


# in order to relate the string with django import http on top

def contact_view(request, *args, **kwarg):
    return render(request, "contact.html", {})
    # return HttpResponse("<h1 style='color:green'>Conatct I will succeed and be health and reach</h1>")


# instead of writing basic html strings, we use django shortucts as it is imported

def about_view(request, *args, **kwarg):
    my_context = {
        'my_text': 'This is about us',
        'this_is_true' : True,
        'my_number': 123,
        'my_list' : [1,2,3,4,"abcd"],
        'my_html':"<h1>Hello World</h1>"
    }
    return render(request, "about.html", my_context)
