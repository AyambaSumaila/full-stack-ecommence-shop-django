from django import forms 

PRODUCT_QUANTITY_CHOICES =[(i, str(i)) for  i in (1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    
    override = forms.BooleanField(
        required=False, 
        initial=False,
        label='Override quantity',
        widget=forms.HiddenInput
    )