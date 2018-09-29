from django import forms


class PlayerFrom(forms.Form):
    nick = forms.CharField(min_length=5, max_length=15, label="Apodo")