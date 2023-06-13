from django import forms
# from seller.models import Seller_books 
from .models import buyer_data
# Subject , Year ,
# Seller_books, City

class Buyer_booksForm(forms.ModelForm):
    class Meta:
        model = buyer_data
        fields = ['year', 'sem', 'sub']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['sub'].queryset = Subject.objects.none()

    #     if 'year' in self.data:
    #         try:
    #             year_id = int(self.data.get('year'))
    #             self.fields['sub'].queryset = Subject.objects.filter(year_id=year_id)
    #             # .order_by('subject')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['sub'].queryset = self.instance.year.subject_set
    #         # .order_by('name')