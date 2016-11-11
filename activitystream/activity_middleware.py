from anotherapp.models import Employee
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from datetime import date
from .models import Stream
uname=""

def ActivityMiddleware(get_response):

	def middleware(request):
		global uname
		uname=request.user.username
		response = get_response(request)
		return response

	return middleware
	

@receiver(post_save, sender=Employee)
def save_handler(sender, instance, created, **kwargs):
	
	if created==True:
		message="Employee {} has been added by {} at {}".format(instance,uname,date.today())
		s=Stream(value=message)
		s.save()
	else:
		message="Employee {} has been updated by {} at {}".format(instance,uname,date.today())
		s=Stream(value=message)
		s.save()

@receiver(pre_delete, sender=Employee)
def delete_handler(sender, instance, **kwargs):
	message="Employee {} has been deleted by {} at {}".format(instance,uname,date.today())
	s=Stream(value=message)
	s.save()

		