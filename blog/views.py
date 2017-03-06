from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.
from datetime import datetime
from blog.models import BlogPost
#from django.template import loader,Context
from django.http import HttpResponseRedirect
#def blog(request):
#    posts = BlogPost.objects.all()
#    t = loader.get_template("blog.html")
#    c = Context({'posts':posts})
#    return HttpResponse(t.render(c))
def blog(request):
    posts = BlogPost.objects.all()
    return render_to_response('blog.html',{'posts':posts,},RequestContext(request))

def create_blogpost(request):
    if request.method == 'POST':

        BlogPost(
            title = request.POST.get('title'),
            body = request.POST.get('body'),
            timestamp = datetime.now(),
        ).save
    return HttpResponseRedirect('/blog/')
