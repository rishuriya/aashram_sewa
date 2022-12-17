from django import forms

from .models import user_form

class UserForm(forms.ModelForm):

    class Meta:
        model = user_form
        fields = ('first_name','second_name','spritual_name', 'email', 'phone','date_of_arrival','time_of_help','duration_of_help','help_on_departure','special_skill','previous_volunteering_department','hour_of_help','primary_manager','area_of_management','register_for_seva','type_of_seva','seva_preference','age','sleep_dormitory','message','privacy_policy','suscribe_to_newsletter') 