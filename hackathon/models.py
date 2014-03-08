from django.db import models

# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    mobile = models.CharField(max_length=10,null=True,blank=True,validators=[validate_mobile])
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    department = models.ForeignKey(Department,null=True,blank=True,default=1)
    hostel = models.ForeignKey(Hostel,null=True,blank=True,default=1)
    year = models.ForeignKey(Year,null=True,blank=True,default=1)
    ldap_username = models.CharField(max_length=20,null=True,blank=True)
    rollno=models.CharField(max_length=20,null=True,blank=True)
    alternate_email = models.EmailField(null=True,blank=True)
    room = models.CharField(max_length=10)
    skill = models.ManyToManyField(Skill,null=True,blank=True)
    photo = ImageCropField(max_length=100,upload_to='documents/%Y/%m/%d',blank=True,null=True)
    cropping = ImageRatioField('photo', '150x200',size_warning=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.first_name
    
    @property
    def is_staff(self):
        return self.is_admin

    def __unicode__(self):
        if self.ldap_username:
            return self.ldap_username
        else:
            return "admin"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_superuser(self):
        return self.is_admin
