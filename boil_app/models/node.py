from django.db import models
from django.utils.translation import ugettext_lazy as _

from boil_app.models import TimeStampedModel


class NodeQuerySet(models.QuerySet):
    def vms(self):
        return self.filter(is_vm=True)


class Node(TimeStampedModel):
    STATUS_ENUM = ((0, _("Healthy")), (2, _("Critical")), (3, _("Warning")), (4, _("Unknown")))
    POWER_STATUS = ((0, _("On")), (1, _("Off")), (2, _("Cycle")), (3, _("Unknown")))

    serial_number = models.CharField(_('Serial Number'), max_length=255, unique=True)
    uuid = models.CharField(
        verbose_name=_('UUID'),
        help_text=_('Node UUID'),
        max_length=50,
        null=True, blank=True,
        unique=True,
    )
    blade_slot = models.IntegerField(_('Blade Slot'), blank=True, null=True)

    hostname = models.CharField(
        verbose_name=_('Hostname'),
        max_length=255,
        blank=True, null=True
    )
    ip_address = models.GenericIPAddressField(_('ip address'), null=True, blank=True)

    management_ip_address = models.GenericIPAddressField(
        verbose_name=_('management ip address'),
        help_text=_('IP address for BMC or console access.'),
        blank=True, null=True,
    )

    status = models.IntegerField(_('status'), choices=STATUS_ENUM, default=4, null=True)
    power_status = models.IntegerField(_('power status'), choices=POWER_STATUS, null=True, default=3)

    asset_tag = models.CharField(_('asset tag'), max_length=64, null=True, blank=True)
    firmware = models.CharField(_('firmware'), max_length=50, blank=True, null=True)

    is_vm = models.BooleanField(default=False)

    objects = NodeQuerySet.as_manager()

    def __unicode__(self):
        return '{}'.format(self.serial_number)

    def __str__(self):
        return '{}'.format(self.serial_number)

    class Meta:
        ordering = ['hostname']
