from django.shortcuts import render, get_object_or_404, redirect
from .models import ShortURL
from .forms import ShortURLForm

# DRF imports
from rest_framework import viewsets
from .serializers import ShortURLSerializer

# ---------------------------
# Formulaire HTML / Redirection
# ---------------------------
def shortener_form(request):
    form = ShortURLForm(request.POST or None)
    short_url = None
    if request.method == 'POST' and form.is_valid():
        short_obj = form.save(commit=False)
        if request.user.is_authenticated:
            short_obj.owner = request.user
        short_obj.save()
        short_url = request.build_absolute_uri('/') + short_obj.code + '/'

    if request.user.is_authenticated:
        links = ShortURL.objects.filter(owner=request.user).order_by('-created_at')
    else:
        links = ShortURL.objects.none()

    return render(request, 'shortener/shortener_form.html', {
        'form': form,
        'short_url': short_url,
        'links': links
    })

def redirect_short(request, code):
    short_obj = get_object_or_404(ShortURL, code=code)
    short_obj.visits += 1
    short_obj.save()
    return redirect(short_obj.original_url)

# ---------------------------
# DRF API ViewSet
# ---------------------------
class ShortURLViewSet(viewsets.ModelViewSet):
    queryset = ShortURL.objects.all().order_by('-created_at')
    serializer_class = ShortURLSerializer
