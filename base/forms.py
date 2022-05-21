from cProfile import label
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
        labels = {
            "name" : "Tên Sinh Viên",
            "username" : "Mã Sinh Viên"
        }


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'major']
        labels = {
            "name" : "Tên Sinh Viên",
            "username" : "Mã Sinh Viên",
            "email" : "Email",
            "major" : "Chuyên ngành"
        }
        
