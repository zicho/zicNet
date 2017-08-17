from django import forms

class Feed_entryForm(forms.Form):

    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder' : 'Write your message here.', 'onfocus' : 'this.placeholder = ""', 'onblur' : 'this.placeholder = "Write your message here."', 'class' : 'textfield'}), label='')