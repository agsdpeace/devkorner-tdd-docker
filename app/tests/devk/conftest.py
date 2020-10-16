import pytest

from devk.models import Team, Message, DevkornerInfos


@pytest.fixture(scope='function')
def add_team():
    def _add_team(name, position, biography, linkedin, twitter):
        team = Team.objects.create(name=name, position=position, biography=biography, linkedin=linkedin, twitter=twitter)
        return team
    return _add_team


@pytest.fixture(scope='function')
def add_message():
    def _add_message(name, email, phone_number, country, message):
        message = Message.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            country=country,
            message=message,
        )
        return message
    return _add_message


@pytest.fixture(scope='function')
def add_devkorner_infos():
    def _add_devkorner_infos(name, email, phone_number, facebook, twitter, instagram, linkedin):
        message = DevkornerInfos.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            facebook=facebook,
            twitter=twitter,
            instagram=instagram,
            linkedin=linkedin,
        )
        return message
    return _add_devkorner_infos
