from django import forms


class SubjectForm(forms.Form):
    name = forms.CharField()
    test_date = forms.DateField()
    symptoms = forms.BooleanField()