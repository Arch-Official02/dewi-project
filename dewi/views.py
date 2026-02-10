from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'dewi/index.html')
def index(request):
	return render(request, 'dewi/index.html')	
def service(request):
	return render(request, 'dewi/service.html')
def error_404(request):
	return render(request, 'dewi/404.html')
def blog(request):
	return render(request, 'dewi/blog.html')
def team(request):
	return render(request, 'dewi/team.html')
def project(request):
	return render(request, 'dewi/project.html')
def contact(request):
	return render(request, 'dewi/contact.html')
def about(request):
	return render(request, 'dewi/about.html')
def testimonial(request):
	return render(request, 'dewi/testimonial.html')

