from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import json

# Application Views

# Home
def home_page(request):
	return render(request, 'website/home_page.html')

# Profile
@login_required
def profile(request):
	return render(request, 'website/profile.html')

def room(request, room_name):
    return render(request, 'website/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
