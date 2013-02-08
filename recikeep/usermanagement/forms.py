from django import forms
from .models import User


class CustomValidationModelFormMixin(forms.ModelForm):
    def do_custom_validation(self, cleaned_data):
        pass

    def clean(self):
        cleaned_data = super(CustomValidationModelFormMixin, self).clean()
        self.do_custom_validation(cleaned_data)
        return cleaned_data


class PreSaveModelFormMixin(forms.ModelForm):
    def do_before_save(self, model_instance, cleaned_data):
        pass

    def save(self, commit=True):
        model_instance = super(PreSaveModelFormMixin, self).save(commit=False)

        self.do_before_save(model_instance, self.cleaned_data)
        if commit:
            model_instance.save()
        return model_instance


class UserCreationForm(CustomValidationModelFormMixin, PreSaveModelFormMixin):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email", )

    def do_custom_validation(self, cleaned_data):
        email = cleaned_data.get("email")
        self.password1 = cleaned_data.get("password1")
        self.password2 = cleaned_data.get("password2")

        if self.password1 and self.password2 and self.password1 != self.password2:
            raise forms.ValidationError("Passwords don't match, please try again.")

        if User.objects.find_user_by_email(email):
            raise forms.ValidationError("A user with that email already exists, please try again.")

    def do_before_save(self, model_instance, cleaned_data):
        model_instance.set_password(cleaned_data["password1"])
        model_instance.username = model_instance.email
