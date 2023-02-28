from django import forms

class EntryForm(forms.Form):

    GRADES = [
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ]

    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    school = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your School"
        })
    )
    grade = forms.ChoiceField(
        choices=GRADES,
        max_length=100,
        widget=forms.ChoiceWidget(attrs={
            "class": "form-control",
            "placeholder": "Your Grade"
        })
    )
    email = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your School"
        })
    )
    file = forms.FileField(
        max_length=100,
        widget=forms.FileInput(attrs={
            "class": "form-control",
            "placeholder": "Your File"
        })
    )