from django import forms


class CreateNew(forms.Form):
	name= forms.CharField(label="Name", max_length=200)
