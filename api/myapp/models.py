from django.db import models


# Create your models here.


class Task(models.Model):
    # task title
    title = models.CharField(max_length=255, null=False)
    # name of assignee
    assignee = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.assignee)

    class Meta:
        ordering = ('title',)
