from django import forms
from home.models import Post


class PostFrom(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'author', 'image', 'content')

        widgets = {
            'title':forms.TextInput(),
            'author':forms.TextInput(),
            'content':forms.Textarea(),
        }
