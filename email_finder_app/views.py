from django.shortcuts import render

from .forms import TextInputForm
from .customfunctions import get_list_of_emails


# Create your views here.
def email_finder_view(request):
    emails = []
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            emails = get_list_of_emails(form.cleaned_data['text_input'])
    else:
        form = TextInputForm()

    return render(request, 'email_finder_app/email_finder_home.html', {'form': form, 'emails': emails})