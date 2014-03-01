from django import forms


class BuyForm(forms.Form):
    email = forms.EmailField(required=True)
