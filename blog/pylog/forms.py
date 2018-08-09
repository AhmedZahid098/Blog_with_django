from django import forms
from .models import Comment


class EmailPostForms(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

    # def clean(self):
    #     cleaned_data = super(CommentForm, self).clean()
    #     name = cleaned_data.get('name')
    #     email = cleaned_data.get('email')
    #     message = cleaned_data.get('body')
    #     if not name and not email and not body:
    #         raise forms.ValidationError('You have to write something!')
