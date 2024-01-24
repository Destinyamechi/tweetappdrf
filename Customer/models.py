from django.db import models
from users.models import CustomUser

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True) 
    bio = models.CharField(max_length = 70, blank=True, null=True)
    # image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')

    def __str__(self):
         return f'{self.user.username} Profile'
    
    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)

    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)