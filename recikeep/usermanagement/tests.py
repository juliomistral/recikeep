from .forms import UserCreationForm

from django import forms

from flexmock import flexmock
from unittest import TestCase


class UserCreationFormTest(TestCase):
    """
    UserCreationForm: Handles input for creating a user at signup
    """
    def setUp(self):
        self.data = {
            "email" : "test@test.com",
            "password1" : "foo",
            "password2" : "bar"
        }

    def test_fails_when_passwords_dont_match(self):
        """Should fail when the password and the confirm password don't match"""
        form = UserCreationForm(data=self.data)
        self.assertRaises(forms.ValidationError, form.do_custom_validation, self.data)

    def test_should_set_username_to_email(self):
        """Should set the username to the email before saving the new user"""
        mocked_user = flexmock(email="test@test.com").should_receive("set_password").and_return(None).mock()
        form = UserCreationForm()
        form.do_before_save(mocked_user, self.data)

        self.assertEqual(mocked_user.username, "test@test.com")

    def test_should_persist_new_user_on_validation_success(self):
        """Should encrypt the password before saving the new user"""
        mocked_user = flexmock(email="test@test.com").should_receive("set_password").once().and_return(None).mock()
        form = UserCreationForm()
        form.do_before_save(mocked_user, self.data)

