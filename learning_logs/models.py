# from django.db import models 
#
# class Topic(models.Model):
#   # a topic that the user is learning about
#     topic1 = models.ForeignKey("Topic", on_delete=models.CASCADE)
#     text = models.TextField(max_length=200)
#     date_added =  models.DateTimeField(auto_now_add=True) 
# class Entry(models.Model):
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE) 
#     text = models.CharField(max_length=200)  
#     date_added = models.DateTimeField(auto_now_add=True)
# class Meta:
#         verbose_name_plural = 'entries'
# def __str__(self):
#         """ return a string representing the model."""
#         return self.text[:50] + "..."
#
#*********** original ***********
from django.db import models
class Topic(models.Model):
    # a topic that the user is learning about
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Entry(models.Model):
    #topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + "..." 

# ************* end Original *********