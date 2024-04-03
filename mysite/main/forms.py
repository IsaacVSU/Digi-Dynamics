from django import forms
from .choices import GameSearch_CHOICES, GENRE_CHOICES


class Games(forms.Form):
    name = forms.CharField(label="", max_length=200, widget=forms.TextInput(
            attrs={
                "class": "searchForm",
                "placeholder": "Enter Game Name",
                "id": "placeholderName"
            }
        ),
    )
    genres = forms.MultipleChoiceField(choices=GENRE_CHOICES, label="Genres", widget=forms.CheckboxSelectMultiple(
        attrs={
            "id" : "GameGenres",
            "class" : "searchForm",
        }
        ),
    )


    SearchBy = forms.ChoiceField(choices=GameSearch_CHOICES, label="Search by", 
                                    widget=forms.Select(
                                         attrs={
                                            'id': 'searchBy'
                                            }
                                        )
                                )
    #NSFW = forms.BooleanField(required=False, label="NSFW")

class Music(forms.Form):
    name = forms.CharField(label="Song name", max_length=200, widget=forms.TextInput(
            attrs={
                "class": "searchForm",
                "placeholder": "Enter Soundtrack Name",
            }
        ),
    )

class DLC(forms.Form):
    name = forms.CharField(label="", max_length=200, widget=forms.TextInput(
            attrs={
                "class": "searchForm",
                "placeholder": "Enter DLC Name",
            }
        ),
    )

class Demo(forms.Form):
    name = forms.CharField(label="", max_length=200, widget=forms.TextInput(
            attrs={
                "class": "searchForm",
                "placeholder": "Enter Demo Name",
            }
        ),
    )
