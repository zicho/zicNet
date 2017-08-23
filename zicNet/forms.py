from django import forms

class Feed_entryForm(forms.Form):

    body = forms.CharField(widget=forms.Textarea(attrs={'rows' : 2, 'placeholder' : 'Write your message here.', 'onfocus' : 'this.placeholder = ""', 'onblur' : 'this.placeholder = "Write your message here."', 'class' : 'textfield'}), label='')
	
class Feed_commentForm(forms.Form):

    body = forms.CharField(widget=forms.Textarea(attrs={'rows' : 2, 'placeholder' : 'Write your comment here.', 'onfocus' : 'this.placeholder = ""', 'onblur' : 'this.placeholder = "Write your comment here."', 'class' : 'textfield'}), label='')