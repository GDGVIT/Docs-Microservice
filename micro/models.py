from django.db import models

class Micro(models.Model):
    link_id = models.CharField(max_length=20)
    link_name = models.URLField()
    link_description = models.TextField()
    link_author = models.CharField(max_length=15)
    class Meta:
        db_table = "micro"