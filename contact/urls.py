from django.urls import path
from .views import contactView

urlpatterns = [
		path("contact/", contactView.as_view(), name = "contact_page"),
		
		]
