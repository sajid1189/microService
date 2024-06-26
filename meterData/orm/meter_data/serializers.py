
from rest_framework import serializers

from .models import ObisChannelChoices, ReadingTypeChoices, Data, ReadingReasonChoices

class MeterReadingSerializer(serializers.ModelSerializer):
    reading_reason = serializers.ChoiceField(choices=ReadingReasonChoices.choices, required=True)

    class Meta:
        model = Data
        fields = (
            "meter_serial",
            "timestamp",
            "channel",
            "value",
            "source",
            "reading_reason",
        )