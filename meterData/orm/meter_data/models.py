from django.db import models

# Create your models here.

class ObisChannelChoices(models.IntegerChoices):
    ENERGY_METER_READING_IMPORT = 1, "1.8.0"  # "Stromzählerstand Bezug"
    ENERGY_METER_READING_EXPORT = 2, "2.8.0"  # "Stromzählerstand Lieferung"


class ReadingTypeChoices(models.TextChoices):

    SMARTMETER = "s", "Fernauslesung"
    MANUALLY = "m", "Manuell"
    ESTIMATED = "e", "Geschätzt"
    INVALID = "i", "Ungültig"


class ReadingReasonChoices(models.TextChoices):
    INSTALLATION = "installation_reading", "Einbauzählerstand"
    DEINSTALLATION = "deinstallation_reading", "Ausbauzählerstand"
    MIDWAY = "midway_reading", "Zwischenablesung"
    CONTRACT_START = "contract_start", "MaKo Wechsel Stilllegung"
    CONTRACT_END = "contract_end", "MaKo Wechsel Drittbelieferung"


class Data(models.Model):
    id = models.BigAutoField(primary_key=True)
    meter_serial = models.CharField(max_length=20)
    channel = models.IntegerField(
        choices=ObisChannelChoices.choices, blank=False, null=False,
    )
    timestamp = models.DateTimeField(null=False)
    value = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    source = models.CharField(
        choices=ReadingTypeChoices.choices,
        default=ReadingTypeChoices.SMARTMETER,
        max_length=1,
        db_index=True,
    )
    reading_reason = models.CharField(
        choices=ReadingReasonChoices.choices,
        blank=True,
        null=True,
        max_length=64,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("channel", "meter_serial", "timestamp", "source"),
                name="unique_channel_meter_timestamp_source",
            ),
        ]
        indexes = [
            models.Index(fields=["meter_serial", "timestamp"]),
            models.Index(fields=["channel", "meter_serial", "timestamp"]),
        ]
        verbose_name = "Datenpunkt"
        verbose_name_plural = "Datenpunkte"
