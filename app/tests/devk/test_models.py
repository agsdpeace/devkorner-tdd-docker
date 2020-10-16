import pytest

from devk.models import Team, Message, DevkornerInfos


# To enable database access in tests
@pytest.mark.django_db
def test_team_model():
    team = Team(
        name='Abdoul BAH',
        position='Full Stack Developer',
        biography='Keep it simple!',
        linkedin='https://www.linkedin.com/in/abdoul-bah/',
        twitter='https://www.linkedin.com/in/abdoul-bah/'
    )
    team.save()
    assert team.name == 'Abdoul BAH'
    assert team.position == 'Full Stack Developer'
    assert team.biography == 'Keep it simple!'
    assert team.linkedin == 'https://www.linkedin.com/in/abdoul-bah/'
    assert team.twitter == 'https://www.linkedin.com/in/abdoul-bah/'
    assert str(team) == team.name


@pytest.mark.django_db
def test_message_model():
    message = Message(
        name='Client',
        email='client@client.com',
        phone_number='0781437818',
        country='Guinea',
        message='I would like to speak to you',
    )
    message.save()
    assert message.name == 'Client'
    assert message.email == 'client@client.com'
    assert message.phone_number == '0781437818'
    assert message.country == 'Guinea'
    assert message.message == 'I would like to speak to you'
    assert str(message) == message.name


@pytest.mark.django_db
def test_devkorner_infos_model():
    devkorner_infos = DevkornerInfos(
        name='Dev Korner',
        email='contact@devkorner.fr',
        phone_number='0781437818',
        facebook='facebook',
        twitter='twitter',
        instagram='instagram',
        linkedin='linkedin',
    )
    devkorner_infos.save()
    assert devkorner_infos.name == 'Dev Korner'
    assert devkorner_infos.email == 'contact@devkorner.fr'
    assert devkorner_infos.phone_number == '0781437818'
    assert devkorner_infos.facebook == 'facebook'
    assert devkorner_infos.twitter == 'twitter'
    assert devkorner_infos.instagram == 'instagram'
    assert devkorner_infos.linkedin == 'linkedin'
    assert str(devkorner_infos) == devkorner_infos.name

