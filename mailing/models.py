from django.db import models

class EmailTemplate(models.Model):
    subject = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.subject
    