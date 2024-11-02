from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AeroportViewSet, GateViewSet, FlightViewSet, PassengerViewSet, TicketViewSet

router = DefaultRouter()
router.register(r'aeroport', AeroportViewSet)
router.register(r'gates', GateViewSet)
router.register(r'flights', FlightViewSet)
router.register(r'passengers', PassengerViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
