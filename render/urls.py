from django.urls import path

from render.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="render-index"),
]
