from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


# CUSTOM CLEARABLE FILE INPUT
class CustomClearableFileInput(ClearableFileInput):
    """ Defines a custom file input widget,
        with customized labels and specify template"""
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'