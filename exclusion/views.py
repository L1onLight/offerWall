from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from exclusion.models import Exclusion
from exclusion.serializers import ExclusionSerializer, ExcludedOffersSerializer, ExcludedOffersRequestParamSerializer


# Create your views here.
@extend_schema(tags=["Exclusion"])
class ExclusionViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ExclusionSerializer
    queryset = Exclusion.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance, created = Exclusion.objects.get_or_create(click_id=serializer.validated_data["click_id"])
            instance.exclude_offer(serializer.validated_data["offer_id"])
            instance.save()
            return Response({"message": "Exclusion created"}, status=201)
        return Response(serializer.errors, status=400)

    @extend_schema(parameters=[ExcludedOffersRequestParamSerializer])
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.query_params.get("is_array") == "true":
            return Response({"excluded_offers": [int(i) for i in instance.excluded_offers.split(",")]})
        serializer = ExcludedOffersSerializer(instance=instance)
        return Response(serializer.data)
