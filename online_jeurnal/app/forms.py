from django import forms

class CreateForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    surname = forms.CharField(label='Surname', max_length=50)
    subj = forms.ChoiceField(label='Subject', choices=(
        (1, "Biology"),
        (2, "Physics"),
        (3, "Russian"),
        (4, "Geography"),
        (5, "Math"),
    ))
    score = forms.ChoiceField(label='Score', choices=(
        (1, '2'),
        (2, '3'),
        (3, '4'),
        (4, '5')
    ))
    gpa = forms.FloatField(label='GPA')