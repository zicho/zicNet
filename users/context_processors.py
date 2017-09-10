from users.models import private_message
import json

def unread_messages_check(request):

    if request.user.is_authenticated():
        
        unread_messages = private_message.objects.all().filter(recipient=request.user).filter(unread=True)
    
        js_unread_messages = json.dumps(len(unread_messages))
       
        return {'unread_messages': unread_messages, 'js_data' : js_unread_messages}
		
    else:
	
        return {'unread_messages': 0, 'js_data' : 0}
	
    