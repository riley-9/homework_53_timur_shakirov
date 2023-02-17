from django.db import models


class Task(models.Model):
    STATUSES = (('new', 'New'), ('in_progress', 'In progress'), ('done', 'Done'))
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Title')
    description = models.TextField(max_length=300, null=False, blank=False, verbose_name='Description')
    status = models.CharField(max_length=20, choices=STATUSES, null=False, blank=False, default='new', verbose_name='Status')
    deadline = models.CharField(max_length=30, null=True, blank=True, default='', verbose_name='Deadline')

    def __str__(self):
        return self.title
