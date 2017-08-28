from django.shortcuts import render
  # the index function is called when root is visited

def index(request):
    return render(request, 'hello_app/index.html')
