from rest_framework.viewsets import ModelViewSet
from .serializers import ElementSerializer
from table.models import Element

class ElementViewSet(ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    http_method_names = ['get','head','list']
    filter_fields = ('element','symbol','atomicNumber','atomicMass','neutrons',
                       'protons','electrons','phase','radioactive','tp')





