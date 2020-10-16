import pytest

from devk.models import Team, Message


@pytest.fixture(scope='function')
def add_team():
    def _add_team(name, position, biography, linkedin, twitter):
        team = Team.objects.create(name=name, position=position, biography=biography, linkedin=linkedin, twitter=twitter)
        return team
    return _add_team


@pytest.fixture(scope='function')
def add_message():
    def _add_message(name, email, phoneNumber, country, message):
        message = Message.objects.create(
            name=name,
            email=email,
            phoneNumber=phoneNumber,
            country=country,
            message=message,
        )
        return message
    return _add_message
