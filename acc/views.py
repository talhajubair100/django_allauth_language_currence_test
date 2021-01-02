from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

import djauth
# from allauth.account.views import SignupView
# from .models import EmployeUser
# from djauth.forms import CustomeCompanySignupForm
# from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from .models import Post
from djauth import settings

# Create your views here.
@login_required
def home(request):
    if not request.session.has_key('currency'):
        request.session['currency'] = settings.DEFAULT_CURRENCY

    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'home.html', context)
 
def selectcurrency(request):
    lasturl = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        request.session['currency'] = request.POST['currency']
    return HttpResponseRedirect(lasturl)