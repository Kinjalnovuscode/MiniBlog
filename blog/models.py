from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Use ForeignKey for better relationships
    title = models.CharField(max_length=100)
    desc = models.TextField()
    post_id = models.IntegerField(null=True, blank=True, unique=True)

def save(self, *args, **kwargs):
    if not self.post_id:  # Only generate post_id if it doesn't exist
        last_post = Post.objects.order_by('post_id').last()
        if last_post:
            self.post_id = last_post.post_id + 1
        else:
            self.post_id = 1  # First post
    super().save(*args, **kwargs)


def get_default_user():
    # Replace '1' with the ID of your desired default user
    return User.objects.first().id if User.objects.exists() else 1