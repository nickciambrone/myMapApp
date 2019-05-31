from django import forms
from houses.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author', 'address', 'beds','baths','house_pic')
        widgets = {
            'address':forms.TextInput(attrs={'class':'textinputclass'}),
            'beds':forms.TextInput(attrs={'class':'textinputclass'}),
            'baths':forms.TextInput(attrs={'class':'textinputclass'}),

        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }
