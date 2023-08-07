from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

class UserManager(BaseUserManager):
    
    
    def create_user(self, email, username, password=None):

        if not email:
            raise ValueError('Un utilisateur doit avoir une address')
        
        if not password:
            raise ValueError('Un utilisateur doit avoir un mot de pass')

         
        user        = self.model(
        email       = self.normalize_email(email=email),
        username    = username,
        password    = password
        )

        user.set_password(password)
        user.save(using=self._db)


        return user


    def create_superuser(self, email, username, password):

       user          = self.create_user(
            email    = email,
            username = username,
            password = password
            )

       user.is_admin = True
       user.is_staff = True
       user.is_superuser = True
       
       user.save(using=self._db)
       
       return user

       

class GuideUser(AbstractBaseUser):

    username 				= models.CharField(max_length=30, unique=True)
    email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)


    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):

        return self.is_admin

    def has_module_perms(self,app_label):

        return True

    # 679202310  blondie
    
    
class Profil_User(models.Model):
    
    user       = models.ForeignKey(GuideUser, blank=True, on_delete=models.CASCADE)
    image       = models.ImageField(upload_to="uploads/profile", blank=True, null=True)



        

    



	
        
        

        

        

