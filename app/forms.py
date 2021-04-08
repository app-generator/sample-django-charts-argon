from django import forms

from app.models import Order


class OrderForm(forms.ModelForm):
    product_name = forms.CharField(label="Product Name", widget=forms.TextInput(attrs={'class': 'form-control order'}))
    price = forms.FloatField(label="Price", widget=forms.TextInput(attrs={'class': 'form-control order'}))

    class Meta:
        model = Order
        fields = ['product_name', 'price']
