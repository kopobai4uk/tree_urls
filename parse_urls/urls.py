from django.urls import path
from .views import GetUrlToParse
urlpatterns = [
    path('', GetUrlToParse.as_view()),
]