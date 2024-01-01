from django.contrib import admin

from  learning_logs.models import Topic , Entry
#from .models import Topic , Entry
# Register your models here.
# from .models import Topic
admin.site.register(Topic)
admin.site.register(Entry)


"""from learning_logs.models import Topic, Entry
"""