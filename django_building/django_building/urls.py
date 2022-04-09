from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('building_business_card.urls', 'building_business_card'), namespace='pl')),
    path('ru/', include(('building_rus.urls', 'building_rus'), namespace='ru')),
    path('en/', include(('building_eng.urls', 'building_eng'), namespace='en')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)