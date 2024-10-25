from django import forms

class weartherforms(forms.Form):
    city=forms.CharField(max_length=200)