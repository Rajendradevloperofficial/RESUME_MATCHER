from django import forms

class UploadFileForm(forms.Form):
    resume = forms.FileField(label='Upload Resume')
    job_desc = forms.FileField(label='Upload Job Description')