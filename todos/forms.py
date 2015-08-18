from todos.models import Todo
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class TodoForm(forms.ModelForm):
    class Meta: 
        model = Todo
        fields = ('task','description','priority','due_date', 'tag')
    
    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('Save', 'Save', css_class='btn-primary'))
