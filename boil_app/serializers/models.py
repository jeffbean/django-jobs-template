from rest_framework import serializers

from boil_app.models import Node


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node


class AutomationNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        depth = 1
        exclude = ('created_on', 'pod', 'chassis')


class AutomationNodeVMSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        depth = 1
        exclude = ('created_on', 'chassis', 'pod', 'blade_slot', 'firmware', 'asset_tag')
