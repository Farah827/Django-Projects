from django.db import models
import re
from datetime import date
import bcrypt

class UserManager(models.Manager):
    def registration_validator(self,postData):
        errors ={}

        if len(postData['first_name']) < 2 or not postData['first_name'].isalpha():
            errors['first_name'] = "First name must be at least 2 character"

        if len(postData['last_name']) < 2 or not postData['last_name'].isalpha()  :
            errors['last_name'] = "Last name must be at least 2 char"  

        EMAIL_REGEX =  re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"
        if User.objects.filter(email = postData['email']):
            errors['email_unique'] = "This Email already regustered"

        if len(postData['password']) < 8 :
            errors['password'] = "Password must be at least 8 character"    
        if postData['password'] != postData['confirm_password']:
            errors['confirm_pw'] = "Passwords dont match"  

        if postData.get('birthday'):
            try:
                birthday = date.fromisoformat(postData['birthday']) 
            except ValueError:
                errors['birthday'] = "Invalid birthday format"
                return errors  

            if birthday > date.today():
                errors['birthday'] = "Birthday cannot be in the future"
            else:
                age = date.today().year - birthday.year - (
                    (date.today().month, date.today().day) < (birthday.month, birthday.day)
                )
                if age < 13:
                    errors['age'] = "You must be at least 13 years old"
        return errors            

    


    def login_validator(self,postData):
        errors={}
        user = User.objects.filter(email = postData['email']).first()
        if user:
            if not bcrypt.checkpw(postData.get('password', '').encode(), user.password.encode()):
                errors['password'] = "Invalid password"
        else:
            errors['email'] = "Email not found"

        return errors


class User(models.Model):
        first_name = models.CharField(max_length=45)
        last_name = models.CharField(max_length=45)
        email = models.EmailField(unique=True)
        password = models.CharField(max_length=255)
        birthday = models.DateField(null=True, blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        objects = UserManager()
