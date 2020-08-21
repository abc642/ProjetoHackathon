from rest_framework.viewsets import ModelViewSet
from .serializers import ElementSerializer,ComercioSerializer
from table.models import Element,Comercio

class ElementViewSet(ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    http_method_names = ['get','head','list']
    filter_fields = ('element','symbol','atomicNumber','atomicMass','neutrons',
                       'protons','electrons','phase','radioactive','tp')

class ComercioViewSet(ModelViewSet):
    queryset = Comercio.objects.all()
    serializer_class = ComercioSerializer
    http_method_names = ['get','head','list']
    filter_fields = ('titulo','descricao','cidade','numero','tipo','imagem')



