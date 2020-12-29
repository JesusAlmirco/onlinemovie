from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def testimonial(request):
    return render(request, 'testimonial.html', {})