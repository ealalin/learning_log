from django.db import models
from django.utils import timezone

class TextField(models.TextField):
    pass

class Topic(models.Model):
    text = models.CharField(max_length=200)
    # a topic that the user is learning about
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Return a string representing the model."""
        return f"Topic {self.id}"

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = TextField(max_length=200)  # Using the custom TextField
    date_added = models.DateTimeField(auto_now_add=True)
    #date_added = models.DateTimeField(auto_now_add=True, default=timezone.now)


    class Meta:
        verbose_name_plural = 'entries'

   
    def __str__(self):
        """Return a string representing the model."""
        return f"Topic {self.id}"

#*********** original ***********
# from django.db import models
# class Topic(models.Model):
#     # a topic that the user is learning about
#     name = models.CharField(max_length=200)
#     def __str__(self):
#         return self.name
# class Entry(models.Model):
#     #topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     date_added = models.DateTimeField(auto_now_add=True)
#     class Meta:
#         verbose_name_plural = 'entries'
#     def __str__(self):
#         return self.text[:50] + "..." 
# ************* end Original *********
