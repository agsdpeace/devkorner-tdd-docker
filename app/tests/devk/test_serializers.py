from devk.serializers import TeamSerializer, MessageSerializer, DevkornerInfosSerializer


def test_valid_team_serializer():
    valid_serializer_data = {
        'name': 'Abdoul BAH',
        'position': 'Full Stack Engineer',
        'biography': 'Keep it simple!',
        'linkedin': 'https://www.linkedin.com/in/abdoul-bah/',
        'twitter': 'https://www.linkedin.com/in/abdoul-bah/'
    }
    serializer = TeamSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_team_serializer():
    invalid_serializer_data = {
        'name': 'Abdoul BAH',
        'position': 'Full Stack Engineer',
        'biography': 'Keep it simple!',
        'linkedin': 'https://www.linkedin.com/in/abdoul-bah/'
    }
    serializer = TeamSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {'twitter': ['This field is required.']}


def test_valid_message_serializer():
    valid_serializer_data = {
        'name': 'Client',
        'email': 'client@client.com',
        'phone_number': '0781437818',
        'country': 'Guinea',
        'message': 'I would like to speak to you!',
    }
    serializer = MessageSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_message_serializer():
    invalid_serializer_data = {
        'name': 'Client',
        'email': 'client@client.com',
        'phone_number': '0781437818',
        'country': 'Guinea',
    }
    serializer = MessageSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {'message': ['This field is required.']}


def test_valid_devkorner_infos_serializer():
    valid_serializer_data = {
        'name': 'Dev Korner',
        'email': 'contact@devkorner.fr',
        'phone_number': '0781437818',
        'facebook': 'facebook',
        'twitter': 'twitter',
        'instagram': 'instagram',
        'linkedin': 'linkedin',
    }
    serializer = DevkornerInfosSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_devkorner_infos_serializer():
    invalid_serializer_data = {
        'name': 'Dev Korner',
        'email': 'contact@devkorner.fr',
        'phone_number': '0781437818',
        'facebook': 'facebook',
        'twitter': 'twitter',
        'instagram': 'instagram',
    }
    serializer = DevkornerInfosSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {'linkedin': ['This field is required.']}
