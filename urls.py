# from c:\learning_log\urls.py
# ===============working part from 23/12/2023====================#
# from django.contrib import admin
# from django.urls import path
# from learning_logs.views import My_View

# urlpatterns = [
   
#      path("learning_logs/", My_View.as_view(), name="my_view"),
#      path('admin/', admin.site.urls),
# ]
# ===============End working part from 23/12/2023====================#

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('learning_logs.urls', namespace='learning_logs')),
]