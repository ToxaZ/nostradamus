from django import forms
from matches.models import Team


class NewPredictionForm(forms.Form):
    home_score = forms.IntegerField()
    guest_score = forms.IntegerField()


class WinnerPredictionForm(forms.Form):
    team_id = forms.ModelChoiceField(queryset=Team.objects.all())
