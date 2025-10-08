from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import redirect_short, shortener_form, ShortURLViewSet

router = DefaultRouter()
router.register(r'links', ShortURLViewSet, basename='links')

urlpatterns = [
    path('api/', include(router.urls)),  # API REST
    path('', shortener_form, name='shortener_form'),  # Formulaire HTML
    path('<str:code>/', redirect_short, name='redirect_short'),  # Redirection
]
