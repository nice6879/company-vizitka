from django import forms

from .models import Murojaat

class MurojaatForm(forms.ModelForm):

        class Meta:
            model = Murojaat
            fields = ('full_name', 'email', 'tel_nomer', 'murojaat')

