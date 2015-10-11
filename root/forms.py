from django.forms import ModelForm

from .models import Page


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['name', 'title', 'subtitle', 'header_image', 'body']
        exclude = ['edited']

    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs['cols'] = 60
        self.fields['body'].widget.attrs['rows'] = 25