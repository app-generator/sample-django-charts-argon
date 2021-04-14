from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    product_name = forms.CharField(label="Product Name", widget=forms.TextInput(attrs={'class': 'form-control order'}))
    price = forms.IntegerField(label="$ Price", widget=forms.TextInput(attrs={'class': 'form-control order'}))
    created_time = forms.DateTimeField(label="Created Time", widget=forms.TextInput(
        attrs={'class': 'form-control order', 'placeholder': 'YY-mm-dd H:i:s'}))

    class Meta:
        model = Order
        fields = ['product_name', 'price', 'created_time']
