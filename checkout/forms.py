from django import forms

#   Modules from other apps
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        class Meta:
            model = Order
            fields = ('full_name', 'email', 'phone_number',
                      'address', 'city', 'postcode', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #   Add placeholders and classes
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'city': 'City',
            'address': 'Address',
        }

        #   setting autofocus to true
        #   cursor starts in full_name when page is loaded
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False