from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import View
# from django.views import views
# ******** 30/11/2023  add from alain *******
class My_View(View):  # Correct class definition
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")




# ******** end   30/11/2023  add from alain *******