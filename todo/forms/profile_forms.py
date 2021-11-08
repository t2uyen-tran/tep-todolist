from django import forms

from todo.models import Profile

# Form for update profile
class ProfileForm(forms.ModelForm):
    # Add 3 fields from User model to ProfileForm
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

# Form validation to return error message if error happened
def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg
