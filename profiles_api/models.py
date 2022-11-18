from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin, BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Custom Manager for user profiles ( for UserProfile model)"""

    def create_user(self,email,name,password=None):
        """Create and save new user profile"""
        if not email:
            raise ValueError('User must have email address')

        email = self.normalize_email(email)
        user = self.model(email=email,name = name)
        
        # encrypting/hashing password
        user.set_password(password)
        user.save(using=self._db) #good practice so that in future we can use multiple db easily

        return user

    def create_superuser(self,email,name,password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        
        user.save(using = self._db)

        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active= models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    #Creating custom model manager
    objects = UserProfileManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS= ['name']

    def get_full_name(self):
        """Retrieve full name of person"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of person"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Provides status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    ) # best practice to get model from settings if have customized user model
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        """Return string representation"""
        return self.status_text
