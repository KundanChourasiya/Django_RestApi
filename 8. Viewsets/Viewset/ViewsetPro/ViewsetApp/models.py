from django.db import models

class Feedback(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=200, help_text="Name is required")
    email = models.EmailField(max_length=200,unique=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modefied = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name + "-" + self.email
