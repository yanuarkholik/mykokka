from django.forms import ModelForm

from.models import Pesan, Comment

class PesanForm(ModelForm):
    class Meta:
        model = Pesan
        fields = '__all__'

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
    