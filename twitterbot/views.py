from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AccountForm
from django.contrib.auth import get_user_model
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     if request.method == "POST":
#         form = AccountForm(request.POST)
#         user = get_user_model()
#         print(user)
#         if form.is_valid():
#             return HttpResponseRedirect("/")
#     else:
#         form = AccountForm()
#     return render(request, "index.html", {"form": form})

class HomePageView(LoginRequiredMixin, FormView):
    form_class = AccountForm
    template_name = "index.html"
    login_url = "account_login"
    success_url = "/result/"

    def form_valid(self, form: AccountForm) -> HttpResponse:
        username = form.cleaned_data["username"]
        print(username)
        return super().form_valid(form)

class ResultView(LoginRequiredMixin, TemplateView):
    template_name = "result.html"
    login_url = 'account_login'