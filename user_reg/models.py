from django.db import models
# Create your models here.

class User(models.Model):
  username = models.CharField(max_length=15)
  fname = models.CharField(max_length=15)
  lname = models.CharField(max_length=15)
  email = models.EmailField(max_length=15)
  password = models.CharField(max_length=8)
  re_password = models.CharField(max_length=8)

  def __str__(self):
    return self.name
  


# class Relation(models.Model):
#   name = models.CharField(max_length = 25)
  
  # def __str__(self):
  #   return self.name


# class User(models.Model):
#   GENDER_CHOICES = (
#           ('M', 'Male'),
#           ('F', 'Female'),
#       )
#   firstname = models.CharField(max_length=15)
#   lastname = models.CharField(max_length=15)
#   password = models.CharField(max_length=8)
#   mobile = models.CharField(max_length=11)
  # gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
  # relation = models.ForeignKey(Relation,on_delete=models.CASCADE)

  # slug = models.SlugField(unique=True)

  # def save(self, *args, **kwargs):
  #         self.slug = self.slug(self.firstname)
  #         super().save(*args, **kwargs)

