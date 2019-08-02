from django.shortcuts import render

# Render the index page
def index(request):
    return render(request, 'index.html')

# Render test page
def test(request):
    return render(request, 'test.html')
