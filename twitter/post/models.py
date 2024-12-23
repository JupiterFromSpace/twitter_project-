from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length= 100)
    age = models.PositiveIntegerField()
    bio = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name





class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="imageprof/")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Like(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)