from django import forms
from user.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'location','min_distance','max_distance','min_dating_age',
            'max_dating_age','dating_sex','vibration','only_matche','auto_play',
        ]
    def clean_max_dating_age(self):
        cleaned_data = super().clean()
        max_dating_age = cleaned_data['max_dating_age']
        min_dating_age = cleaned_data['min_dating_age']
        if max_dating_age<min_dating_age:
            raise forms.ValidationError('max_dating_age<min_dating_age')
        return max_dating_age

    def clean_max_distance(self):
        cleaned_data = super().clean()
        max_distance = cleaned_data['max_distance']
        min_distance = cleaned_data['min_distance']
        if max_distance < min_distance:
            raise forms.ValidationError('max_distance<min_distance')
        return max_distance