from django import forms
from django.contrib.auth import authenticate, login, logout, get_user_model

User = get_user_model()  # фактически вы создаете экземпляр класса User из django

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')  # забираем текст из поля username
        password = self.cleaned_data.get('password')  # забираем текст из поля username

        if username and password:  # если значения этих переменных не пустые
            user = authenticate(username=username, password=password)  # "залогинить" пользователя с его данными
            if not user:  # если юзер не был найден
                raise forms.ValidationError("User doesn't exist or password is incorrect.")
            if not user.is_active:
                raise forms.ValidationError("Your account has been disabled!")

        return super(UserLoginForm, self).clean()


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        field = [
            "username",
            "email",
            "password",
        ]
