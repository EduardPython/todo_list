from django import forms


class CustomDateInput(forms.DateInput):
    def __init__(self, *args, **kwargs):
        kwargs.update({'attrs': {'type': 'date'}})
        super(CustomDateInput, self).__init__(*args, **kwargs)


class DateTimeForm(forms.Form):
    date_time = forms.DateField(widget=CustomDateInput())
