from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist

from pt.models import PtTest, PtScore
from personnel.models import Cadet


class TestForm(forms.ModelForm):

    class Meta():
        model = PtTest
        exclude = []


class ScoreForm(forms.Form):
    cadet = forms.CharField()
    cadet_id = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'cadet_id'}), required=False)
    pushups = forms.IntegerField(initial=None, widget=forms.NumberInput(attrs={'placeholder': 0}))
    situps = forms.IntegerField(initial=None, widget=forms.NumberInput(attrs={'placeholder': 0}))
    two_mile = forms.CharField(initial=None, widget=forms.TextInput(attrs={'placeholder': '00:00'}))

    invalid_name = ValidationError(
            'Invalid cadet name. Check for spelling and ensure that the cadet has a profile made',
            code='invalid',
    )

    invalid_run_time = ValidationError(
        'Invalid Run Time Format',
        code='invalid'
    )

    def clean_cadet_id(self):
        if not self.cleaned_data.get('cadet_id') and self.cleaned_data.get('cadet'):
            self.add_error('cadet', self.invalid_name)

        try:
            if self.cleaned_data.get('cadet_id'):
                Cadet.objects.get(id=int(self.cleaned_data.get('cadet_id')))
        except ObjectDoesNotExist:
            self.add_error('cadet', self.invalid_name)

        return self.cleaned_data.get('cadet_id')

    def clean_two_mile(self):

        if not PtScore.valid_run_time(self.cleaned_data.get('two_mile')):
            self.add_error('two_mile', self.invalid_run_time)

        return self.cleaned_data.get('two_mile')