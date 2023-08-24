from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, phone, password, **kwargs):
        if not email:
            raise ValueError("Email is required!")

        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, phone, **kwargs):
        if not email:
            raise ValueError("Email is required!")

        kwargs['is_staff'] = True  # даем права суперадмина
        kwargs['is_superuser'] = True
        kwargs['is_active'] = True

        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None  # убираем username из полей
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # указываем какое поле использовать при логине
    REQUIRED_FIELDS = ['phone']

    objects = UserManager()  # указываем нового менеджера

    # def create_activation_code(self):
    #     """
    #     1. hashlib.md5(self.email+ str(self.id)).encode() -> hexdigest
    #     2. get_random_string(58, allowed_char=['which symbols are allowed in this string']
    #     3. UUID
    #     4. datetime.datetime.now() or time.time() 01.01.1970
    #      """
    #     import hashlib
    #     string = self.email + str(self.id)
    #     encode_string = string.encode()
    #     md5_object = hashlib.md5(encode_string)
    #     activation_code = md5_object.hexdigest()
    #     self.activation_code = activation_code


class UserImage(models.Model):
    objects = None
    image = models.ImageField(upload_to='users', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')