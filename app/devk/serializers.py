from rest_framework import serializers
from .models import Team, Message, DevkornerInfos


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'
        read_only_fields = ('id', 'created_date', 'updated_date',)


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('id', 'created_date', 'updated_date')


class DevkornerInfosSerializer(serializers.ModelSerializer):

    class Meta:
        model = DevkornerInfos
        fields = '__all__'
        read_only_fields = ('id', 'created_date', 'updated_date',)
