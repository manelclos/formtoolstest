from django import forms


class NumberOfTicketsForm(forms.Form):
    number = forms.IntegerField()


class PeopleForm(forms.Form):
    name = forms.CharField(max_length=30)


class OtherForm(forms.Form):
    info = forms.CharField(max_length=30)
