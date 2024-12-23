from rest_framework_nested import routers
from .views import ConcessionViewSet, VehiculeViewSet
from django.urls import path, include


router = routers.SimpleRouter()
router.register('concessions', ConcessionViewSet, basename='concession')

concession_router = routers.NestedSimpleRouter(router, 'concessions', lookup='concession')
concession_router.register('vehicules', VehiculeViewSet, basename='concession-vehicule')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(concession_router.urls)),
]