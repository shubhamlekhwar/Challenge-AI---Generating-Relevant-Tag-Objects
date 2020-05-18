from django.conf.urls import url
from .views import PreprocessingText
urlpatterns = [
  url('', PreprocessingText.as_view()),
]