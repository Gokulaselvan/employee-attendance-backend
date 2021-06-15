from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from typing import Dict

# Getting the Current User Model
User = get_user_model()


class CustomUserCreationForm(forms.ModelForm):

    #Overriding the fields with password widget to hide the entered value with dots or Asterisk
    password = forms.CharField(max_length=16, widget=forms.PasswordInput)
    retype_password = forms.CharField(
        max_length=16, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'employee_id'] # Adding the required fields 

    def clean(self) -> Dict[str, any]:
        """Cleaning the data"""

        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        retype_password = cleaned_data.get("retype_password")

        if password is not None and retype_password is not None and password != retype_password:
            self.add_error("retype_password", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        """Overriding the save method to get the add the password with hashing"""

        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):

    # Hashing the password 
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'username', 'employee_id', 'password',
                  'is_active', 'is_admin', 'is_staff', 'is_superuser']

