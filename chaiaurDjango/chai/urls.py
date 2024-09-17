from django.urls import include, path
from . import views
# localhost:8000/chai
# iske baad se isme routing hogi

urlpatterns = [
    path('', views.allchai, name="all_chai"),
    # bhai yeh reloading karta hai
    path("__reload__/", include("django_browser_reload.urls")),
    # isko bas bro sabse last mein rakhna

]
