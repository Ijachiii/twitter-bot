from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AccountForm
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/")
    else:
        form = AccountForm()
    return render(request, "index.html", {"form": form})

# class HomePageView(LoginRequiredMixin, TemplateView):
    form = AccountForm()
    template_name = "index.html"
    login_url = "account_login"