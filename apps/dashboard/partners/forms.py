from oscar.apps.dashboard.partners import forms as base_forms
from django import forms


class PartnerCreateForm(base_forms.PartnerCreateForm):
    class Meta(base_forms.PartnerCreateForm.Meta):
        fields = ('name','email', 'address', 'phone_number')