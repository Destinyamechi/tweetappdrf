from django.db import models
from users.models import CustomUser



# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete = models.SET_NULL,null=True)
    slug = models.SlugField(max_length = 50,blank=True, null = True)
    content = models.TextField(max_length = 100)
    #image = models.ImageField(upload_to='images/', blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f' {self.content}||{self.author}'



class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField(max_length = 100)
    parent_comment = models.ForeignKey('self',on_delete = models.CASCADE,blank=True, null = True)
    comment_slug = models.SlugField(max_length = 50,blank=True, null = True)
    #image = models.ImageField(upload_to='images/', blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        if self.parent_comment is None:
            return f'{self.post} -- [{self.author} - {self.content}]'
        return f'{self.author}  {self.content}'
        

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post = self).count()




class Repost(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'repost_post')
    repost = models.BooleanField(default = False)
    reposted_at = models.DateTimeField(auto_now_add = True)
    repost_author = models.ForeignKey(CustomUser,on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.post}||{self.repost_author}'

    


    
class QouteTweet(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='quotetweet_post')
    repost = models.BooleanField(default = False)
    quote_tweet = models.TextField(max_length = 140)
    reposted_at = models.DateTimeField(auto_now_add = True)
    repost_author = models.ForeignKey(CustomUser,on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.post}||{self.repost_author}'

