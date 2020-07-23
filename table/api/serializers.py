from rest_framework.serializers import ModelSerializer
from table.models import Element


class ElementSerializer(ModelSerializer):
    class Meta:
        model = Element
        fields = ('element','symbol','atomicNumber',
                  'atomicMass','neutrons','protons',
                  'electrons','phase','radioactive','tp')
