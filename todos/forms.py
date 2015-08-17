from todos.models import Todo
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class TodoForm(forms.ModelForm):
    class Meta: 
        model = Todo
        fields = ('task','description','priority','due_date', 'tag')
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))