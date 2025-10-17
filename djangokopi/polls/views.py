from django.http import HttpResponse
def index(request):
	 return HttpResponse("HELLO, WORLD. YOU'RE AT THE POLLS INDEX.")
	 