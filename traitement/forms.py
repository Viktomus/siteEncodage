from django import forms

class SiteForm(forms.Form):
	document = forms.FileField(widget=forms.FileInput(attrs={
		'class': 'custom-file-input'
		}))

# class SiteForm(forms.Form):
# 	document = forms.FileField()