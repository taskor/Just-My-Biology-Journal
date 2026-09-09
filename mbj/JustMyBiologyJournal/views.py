from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CreatePost

# Non-Django imports
from datetime import date # for date in create view
import requests

def index(requests):
    return render(requests, 'JustMyBiologyJournal/index.html')

@login_required
def create(requests):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            form.cleaned_data()
            date = date.today()
            post = CreatePost(title=form.title, body=form.body, date=date)
            post.save()

            success = "Post created"
        else:
            error = "Ivalid input - Try again"

        return render(requests, 'JustMyBiologyJournal/create.html', {
            'success': success,
            'error': error,
            'form': form, 
            })

    else: 
        form = CreatePost()

        return render(requests, 'JustMyBiologyJournal/create.html', {
            'form': form, 
            })

# End of file
