from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'pagename': 'Welcome'}
    return render(request, 'index.html', context)
