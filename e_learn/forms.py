# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.db import transaction
# from django.forms.utils import ValidationError
# from django import forms
# from django.contrib.auth import authenticate, get_user_model, password_validation
# from django.utils.translation import gettext_lazy as _

# from e_learn.models import (Sinh_Vien, Khoa_Hoc, Giang_Vien)

# class ProfileForm(forms.ModelForm):
#     email=forms.EmailField(widget=forms.EmailInput())
#     confirm_email=forms.EmailField(widget=forms.EmailInput())

#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'first_name',
#             'last_name',
#             'email',

#         ]
#     def clean(self):
#         cleaned_data = super(ProfileForm, self).clean()
#         email = cleaned_data.get("email")
#         confirm_email = cleaned_data.get("confirm_email")

#         if email != confirm_email:
#             raise forms.ValidationError(
#                 "Emails must match!"
#             )

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email') 

# class LecturerSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User

#     def __init__(self, *args, **kwargs):
#             super(LecturerSignUpForm, self).__init__(*args, **kwargs)

#             for fieldname in ['username', 'password1', 'password2']:
#                 self.fields[fieldname].help_text = None
                    
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_lecturer = True
#         if commit:
#             user.save()
#         return user
    
# class StudentSignUpForm(UserCreationForm):
#     email = forms.EmailField(max_length=255, help_text='Required. Enter a valid email address.')

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ['email', 'username']

#     def __init__(self, *args, **kwargs):
#             super(StudentSignUpForm, self).__init__(*args, **kwargs)

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_student = True
#         user.save()
#         student = Sinh_Vien.objects.create(user=user)
#         return user