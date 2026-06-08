from django.db import models
from datetime import datetime

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData ,show_id=None):
        errors = {}
        if len(postData.get('title' , '').strip()) < 2 :
            errors['title'] = 'Title should be at least 2 characters'
            
        if len(postData.get('network' , '').strip()) < 3 :
            errors['network'] = 'Network should be at least 3 characters'

        if len(postData.get('description' , '').strip()) > 0 and len(postData.get('description' , '')) < 10 :
            errors['description'] = 'Description should be at least 10 characters'
            
        if postData.get('release_date' , ''):
            release = datetime.strptime(postData['release_date'], "%Y-%m-%d")
            if release > datetime.now():
                errors['release_date'] = 'Release date should be in the past'
        
        # Step 1: search for shows with the same title
        query = Show.objects.filter(title__iexact=postData['title'].strip())

        # Step 2: if update → exclude the current show
        if show_id:
            query = query.exclude(id=show_id)

        # Step 3: if result exists → title is not unique
        if query.exists():
            errors['title'] = 'Title already exists'
        return errors
    
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager() 

    def __str__(self):
        return f"{self.title} ({self.network})"
    

# if Show.objects.filter(title=postData['title']).exists():
#     errors['title'] = 'Title already exists'
# case insensitive
# if Show.objects.filter(title__iexact=postData['title']).exists():
#   errors['title'] = 'Title already exists'