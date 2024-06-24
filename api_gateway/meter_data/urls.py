from django.urls import path

from meter_data.views import MeterReadingsViewSet

urlpatterns = [path("MeterReadings", MeterReadingsViewSet.as_view())]
print(urlpatterns)