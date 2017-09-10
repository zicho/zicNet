from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

class Feed_entryForm(forms.Form):

    body = forms.CharField(max_length=420, widget=forms.Textarea(attrs={
	'rows' : 2,
	'placeholder' : 'Write your message here.',
	'onfocus' : 'this.placeholder = ""',
	'onblur' : 'this.placeholder = "Write your message here."',
	'class' : 'textfield',
	'style' : 'width: 100%; margin-top: 24px; height: 100px;',
	'id' : 'feed_entry_textfield'}), label='')
    
class Feed_commentForm(forms.Form):

    body = forms.CharField(max_length=140, widget=forms.Textarea(attrs={
	'placeholder' : 'Write your comment here.',
	'onfocus' : 'this.placeholder = ""',
	'onblur' : 'this.placeholder = "Write your comment here."',
	'style' : "margin-bottom: 16px; height: 100px; width: 100%;",
	'class' : 'textfield'}),
	label='')
	
class send_messageForm(forms.Form):

    body = forms.CharField(max_length=420, widget=forms.Textarea(attrs={
	'rows' : 2,
	'placeholder' : 'Write your message here.',
	'onfocus' : 'this.placeholder = ""',
	'onblur' : 'this.placeholder = "Write your message here."',
	'class' : 'message_textfield textfield',
	'style' : 'width: 100%' }),
	label='')
		
    recipient = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class':'select_box', 'label':'Recipient:'}))
	
	
class Password_changeForm(PasswordChangeForm):

    old_password = forms.CharField(max_length=140, label='', widget=forms.PasswordInput(attrs={
	'id' : 'id_old_password',
	'placeholder' : 'Old password',
	'onfocus' : 'this.placeholder = ""',
	'onblur' : 'this.placeholder = "Old password"',
	'name' : 'id_old_password',
	'style' : 'width: 100%'
	}))
    
    new_password1 = forms.CharField(max_length=140, label='', widget=forms.PasswordInput(attrs={
	'id' : 'id_new_password2',
	'placeholder' : 'New password',
	'onfocus' : 'this.placeholder = ""',
	'onblur' : 'this.placeholder = "New password"',
	'name' : 'id_new_password1',
	'style' : 'width: 100%'
	}))
    
    new_password2 = forms.CharField(max_length=140, label='', widget=forms.PasswordInput(attrs={
	'id' : 'id_new_password2',
	'placeholder' : 'Confirm new password',
	'onfocus' : 'this.placeholder = ""',
	'onblur' : 'this.placeholder = "Confirm new password"',
	'name' : 'id_new_password2', 
	'style' : 'width: 100%'
    }))