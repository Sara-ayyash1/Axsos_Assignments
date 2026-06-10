from django.db import models
from login_app.models import User
from django.utils import timezone
# Create your models here.

class MessageManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        message_text = postData.get('message', '').strip()
        
        if len(message_text) < 5:
            errors["message"] = "The message must be at least 5 characters long."
            
        return errors
    
    def validate_delete(self, message_id):
        errors = {}
        try:
            message = self.get(id=message_id)
            time_difference = timezone.now() - message.created_at
            difference_in_minutes = time_difference.total_seconds() / 60
            
            if difference_in_minutes > 30:
                errors["delete"] = "You can only delete messages within 30 minutes of posting."
        except self.model.DoesNotExist:
            errors["delete"] = "Message not found."
            
        return errors

class CommentManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        comment_text = postData.get('comment', '').strip()
        
        if len(comment_text) < 2:
            errors["comment"] = "The comment must be at least 2 characters long."
            
        return errors

class Message(models.Model):
    message =models.TextField()
    user = models.ForeignKey(User , related_name='messages' , on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)
    objects = MessageManager()

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User , related_name='comments' , on_delete = models.CASCADE)
    message = models.ForeignKey(Message , related_name='comments' , on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)
    objects = CommentManager()