from django.shortcuts import render
from .forms import EmailForm

# Create your views here.
def chatView(request):
    form = EmailForm()
    context = {'form': form}
    return render(request, 'chat.html', context )


