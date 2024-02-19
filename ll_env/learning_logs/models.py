from django.db import models
from django.utils import timezone
from django.contrib.auth.models  import User

class TextField(models.TextField):
    pass

class Topic(models.Model):
    text = models.CharField(max_length=200)
    # a topic that the user is learning about
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=150)  # Add a field to store the username.

    
    def __str__(self):
        """Return a string representing the model."""
        return f"Topic {self.id}"

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = TextField(max_length=200)  # Using the custom TextField
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        """Return a string representing the model."""
       # return f"Topic {self.id}"
        return self.text[:50] + "..."
