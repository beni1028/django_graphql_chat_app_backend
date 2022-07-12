
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


def get_profile_image_filepath(self, filename):
	return 'profile_images/' + str(self.pk) + '/profile_image.png'

def get_default_profile_image():
	return "/default_profile_image.png"


class User(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	is_a_supervisor			= models.BooleanField(default=False)
	profile_image			= models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)
	# hide_email				= models.BooleanField(default=True)
	reporting_manager		= models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, )
	role					= models.CharField(max_length=30, null=True, blank=True)
	team_name				= models.CharField(max_length=30, null=True, blank=True)
	# date_of_hire			= models.DateTimeField(verbose_name='date of hiring', null=True, blank=True)
	# joining_package			= models.FloatField( null=True, blank=True,)
	phone_number 			= models.IntegerField(null=True, blank=False, unique=True)
	emergency_contact		= models.IntegerField(null=True, blank=False, unique=True)
	# address					= models.CharField(max_length=500, null=True, blank=True)
	# blood_group				= models.CharField(max_length=10, null=True, blank=True)
	first_name				= models.CharField(max_length=15, blank=True, null=True)
	last_name				= models.CharField(max_length=15, blank=True, null=True)
	# middle_name				= models.CharField(max_length=15, blank=True, null=True)
	# fathers_name			= models.CharField(max_length=15, blank=True, null=True)
	# mothers_name			= models.CharField(max_length=15, blank=True, null=True)
	employee_id				= models.CharField(max_length=15, blank=True, null=True)
	# marital_status			= models.BooleanField(default=False)
	# MARRIED = 'married'
	# UNMARIED = 'unmaried'
	
	# CHOICES_Marital_status 	= ((MARRIED, 'Married'),(UNMARIED, 'Unmaried'),)
    
	# marital_status 			= models.CharField(max_length=20,choices=CHOICES_Marital_status,null = True)
	# spouse_name				= models.CharField(max_length=15, blank=True, null=True)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	def __str__(self):
		return self.username

	def get_profile_image_filename(self):
		return str(self.profile_image)[str(self.profile_image).index('profile_images/' + str(self.pk) + "/"):]

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True


class Team(models.Model):
	user 					= models.ForeignKey(User,  on_delete=models.CASCADE, related_name="current_user")
	team_name				= models.CharField(max_length=30, null=True, blank=True)
	reporting_manager		= models.ForeignKey(User, on_delete=models.CASCADE, related_name="account_reporting_manager")
	def __str__(self):
		return self.user.username


class Message(models.Model):
	user 					= models.ForeignKey(User, on_delete=models.CASCADE)
	date_time 				= models.DateTimeField(auto_now_add= True)
	message					= models.CharField(max_length=2000,blank=False,null=True)
	team 					= models.ForeignKey(Team, on_delete=models.CASCADE)
	team_name				= models.CharField(max_length=30, null=True, blank=True)


	# read_status				= models.BooleanField(default=False)
	# recipients				= JSONField(null = True)

	# def read_filter(self):
	# 	if 

	def __str__(self):
		return self.user.username
