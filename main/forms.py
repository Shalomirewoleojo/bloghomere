from django import forms
from django.forms import ModelForm, fields, widgets
from django.forms import TextInput, EmailInput, FileInput, Select, ModelMultipleChoiceField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *

class BlogCreateForm (forms.ModelForm):
    # text = forms.CharField(widget=CKEditorUploadingWidget())
    description = forms.CharField(required=False)

    class Meta:
        model = BlogCreate
        fields = ('author', 'title', 'category', 'image_cover', 'video', 'audio', 'text', 'description')

class CommentForm (forms.ModelForm):
    # post = forms.ModelMultipleChoiceField(queryset=BlogCreate.objects.all())
    # user = forms.ModelMultipleChoiceField(queryset=User.objects.all())

    # def save(self, commit=True):
    #    instance = super().save(commit=False)
    #    bc = self.cleaned_data['blogcreate']
    #    instance.blogcreate = bc[0]
    #    instance.save(commit)
    #    return instance

    class Meta:
        model = Comment
        fields = ('body', 'post', 'user')