from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TwitterAccountCheckedForm
from .demo import prediction
from .models import TwitterAccountsCheck
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.
@login_required
def home(request):
    if request.method == "POST":
        form = TwitterAccountCheckedForm(request.POST)
        if form.is_valid():
            screen_name_ = form.cleaned_data["screen_name"]
            pred = prediction(screen_name_)
            data = TwitterAccountsCheck(screen_name=screen_name_, prediction=pred)
            data.save()
            return render(request, "result.html", {"screen_name": screen_name_, "pred": pred})
    else:
        form = TwitterAccountCheckedForm()
    return render(request, "index.html", {"form": form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Change this to your desired URL
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# class HomePageView(LoginRequiredMixin, FormView):
#     form_class = AccountForm
#     template_name = "index.html"
#     login_url = "account_login"
#     success_url = "/result/"
# 
#     def form_valid(self, form: AccountForm) -> HttpResponse:
#         username = form.cleaned_data["username"]
#         print(username)
#         return super().form_valid(form)

class ResultView(LoginRequiredMixin, TemplateView):
    template_name = "result.html"
    login_url = 'account_login'
