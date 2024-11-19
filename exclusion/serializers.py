from rest_framework import serializers, fields
from rest_framework.exceptions import ValidationError

from exclusion.models import Exclusion


class ExclusionSerializer(serializers.Serializer):
    click_id = serializers.CharField()
    offer_id = fields.IntegerField(required=False)

    def get_values_tuple(self):
        if self.is_valid():
            return [self.validated_data.get(field_name) for field_name in self.fields.keys()]

    def validate(self, attrs):
        print(attrs)
        if not attrs.get("offer_list") and attrs.get("offer_id") is None:
            raise ValidationError("Field offer_list or offer_id is required.")
        return attrs


class ExcludedOffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exclusion
        fields = ["excluded_offers"]


class ExcludedOffersRequestParamSerializer(serializers.Serializer):
    is_array = serializers.BooleanField(default=False)
