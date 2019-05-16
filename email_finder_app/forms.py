from django import forms


class TextInputForm(forms.Form):
    text_input = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        label='Enter some text to find all possible e-mails in it:',
    )
