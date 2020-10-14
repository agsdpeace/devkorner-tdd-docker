from devk.serializers import TeamSerializer


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
