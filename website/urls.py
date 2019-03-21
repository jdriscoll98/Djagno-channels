from django.conf.urls import url

from . import views

# Application Routes (URLs)

app_name = 'website'

urlpatterns = [

	# Home Page
	url(r'^$', views.home_page, name='home_page'),

	# Profile Page
	url(r'^profile$', views.profile, name='profile'),

]
