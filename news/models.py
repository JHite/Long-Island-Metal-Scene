from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
	return self.title