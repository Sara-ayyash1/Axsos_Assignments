from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self , postData):
        errors = {}

        if len(postData.get('name' , '').strip())  <= 5 :
            errors['name'] = "Course Name must be more than 5 characters long!"

        if len(postData.get('description' , '').strip())  <= 15 :
            errors['description'] = "Description must be more than 15 characters long!"
        return errors
    


class Course(models.Model):
    name = models.CharField(max_length = 255 )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Description(models.Model):
    content = models.TextField()
    course = models.OneToOneField(Course , on_delete=models.CASCADE , primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.TextField()
    course = models.ForeignKey(Course , related_name='comments' ,on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)