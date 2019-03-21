from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Application Views

# Home
def home_page(request):
	return render(request, 'website/home_page.html')

# Profile
@login_required
def profile(request):
	return render(request, 'website/profile.html')
