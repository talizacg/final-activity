from rest_framework.response import Response
from rest_framework.decorators import api_view
from.models import item
from.serializer import ItemSerializer
# Create your views here.


@api_view(['GET'])
def getData(request):
    item = item.objects.all()
    serializer = ItemSerializer(ItemSerializer, many=True)
    return Response(serializer.data)
