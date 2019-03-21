from django.conf.urls import url

from . import views

# Application Routes (URLs)

app_name = 'website'

urlpatterns = [

	# Home Page
	url(r'^$', views.home_page, name='home_page'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),

	# Profile Page
	url(r'^profile$', views.profile, name='profile'),

]
