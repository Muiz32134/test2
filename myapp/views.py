from django.shortcuts import render

# Home page view
def home(request):
    context = {
        'title': 'Welcome to SABER',
        'message': 'This is where you fall in love'
    }
    return render(request, 'home.html', context)

# Information page view
def information(request):
    return render(request, 'information.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')
