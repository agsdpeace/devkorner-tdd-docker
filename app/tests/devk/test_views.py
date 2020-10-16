import pytest

from devk.models import Team, Message


@pytest.mark.django_db
def test_add_team(client):
    team = Team.objects.all()
    assert len(team) == 0

    resp = client.post(
        '/api/team/',
        {
            'name': 'Timothé Arnauld',
            'position': 'Full Stack Engineer',
            'biography': 'Keep it complex hein!',
            'linkedin': 'https://www.linkedin.com/in/abdoul-bah/',
            'twitter': 'https://www.linkedin.com/in/abdoul-bah/'
        },
        content_type='application/json'
    )
    assert resp.status_code == 201
    assert resp.data['name'] == 'Timothé Arnauld'

    team = Team.objects.all()
    assert len(team) == 1


@pytest.mark.django_db
@pytest.mark.parametrize('payload, status_code', [
    [{}, 400],
    [{'name': 'Abdoul BAH', 'position': 'Full Stack Engineer'}, 400],
])
def test_add_team_invalid_json(client, payload, status_code):
    team = Team.objects.all()
    assert len(team) == 0

    resp = client.post(
        '/api/team/',
        payload,
        content_type='application/json'
    )
    assert resp.status_code == 400

    team = Team.objects.all()
    assert len(team) == 0


@pytest.mark.django_db
def test_get_single_team(client, add_team):
    team = add_team(name='Abdoul', position='Developer', biography='simple', linkedin='linkedin', twitter='twitter')
    resp = client.get(f'/api/team/{team.id}/')
    assert resp.status_code == 200
    assert resp.data['name'] == 'Abdoul'


@pytest.mark.django_db
def test_get_single_team_incorrect_id(client):
    resp = client.get(f'/api/team/bar/')
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_team(client, add_team):
    team_one = add_team(name='Abdoul', position='Developer', biography='simple', linkedin='linkedin', twitter='twitter')
    team_two = add_team(name='Mountaga', position='CEO', biography='simple', linkedin='linkedin', twitter='twitter')
    resp = client.get(f'/api/team/')
    assert resp.status_code == 200
    assert resp.data[0]['name'] == team_one.name
    assert resp.data[1]['name'] == team_two.name


@pytest.mark.django_db
def test_remove_team(client, add_team):
    team = add_team(name='Abdoul', position='Developer', biography='simple', linkedin='linkedin', twitter='twitter')

    resp = client.get(f'/api/team/{team.id}/')
    assert resp.status_code == 200
    assert resp.data['name'] == 'Abdoul'

    resp_two = client.delete(f'/api/team/{team.id}/')
    assert resp_two.status_code == 204

    resp_three = client.get(f'/api/team/')
    assert resp_three.status_code == 200
    assert len(resp_three.data) == 0


@pytest.mark.django_db
def test_remove_team_incorrect_id(client):
    resp = client.delete(f'/api/team/101/')
    assert resp.status_code == 404


@pytest.mark.django_db
def test_update_team(client, add_team):
    team = add_team(name='Abdoul', position='Developer', biography='simple', linkedin='linkedin', twitter='twitter')

    resp = client.put(
        f'/api/team/{team.id}/',
        {'name': 'Timothee', 'position': 'Developer', 'biography': 'sh', 'linkedin': 'linkedin', 'twitter': 'twitter'},
        content_type='application/json',
    )
    assert resp.status_code == 200
    assert resp.data['name'] == 'Timothee'

    resp_two = client.get(f'/api/team/{team.id}/')
    assert resp_two.status_code == 200
    assert resp_two.data['name'] == 'Timothee'


@pytest.mark.django_db
def test_update_team_incorrect_id(client):
    resp = client.put(f'/api/team/101/')
    assert resp.status_code == 404


@pytest.mark.django_db
@pytest.mark.parametrize('add_team, payload, status_code', [
    ['add_team', {}, 400],
    ['add_team', {'name': 'Abdoul', 'position': 'Developer'}, 400],
], indirect=['add_team'])
def test_update_team_invalid_json(client, add_team, payload, status_code):
    team = add_team(name='Abdoul', position='Developer', biography='simple', linkedin='linkedin', twitter='twitter')

    resp = client.put(
        f'/api/team/{team.id}/',
        payload,
        content_type='application/json',
    )
    assert resp.status_code == status_code


@pytest.mark.django_db
def test_add_message(client):
    message = Message.objects.all()
    assert len(message) == 0

    resp = client.post(
        '/api/message/',
        {
            'name': 'Client',
            'email': 'client@client.com',
            'phone_number': '0781437818',
            'country': 'Guinea',
            'message': 'I would like to speak to you!',
        },
        content_type='application/json',
    )
    assert resp.status_code == 201
    assert resp.data['name'] == 'Client'

    message = Message.objects.all()
    assert len(message) == 1


# TODO: add non happy tests for post request

@pytest.mark.django_db
def test_get_all_messages(client, add_message):
    message_one = add_message(
        name='Client',
        email='client@client.com',
        phone_number='0781437818',
        country='Guinea',
        message='I would like to speak to you'
    )

    message_two = add_message(
        name='Client2',
        email='client2@client.com',
        phone_number='0781437818',
        country='Guinea',
        message='I would like to speak to you'
    )
    resp = client.get('/api/message/')
    assert resp.status_code == 200
    assert resp.data[0]['name'] == message_one.name
    assert resp.data[1]['name'] == message_two.name

# TODO: add non happy tests for get request


@pytest.mark.django_db
def test_get_devkorner_infos(client, add_devkorner_infos):
    devkorner_infos = add_devkorner_infos(
        name='Dev Korner',
        email='contact@devkorner.fr',
        phone_number='0781437818',
        facebook='facebook',
        twitter='twitter',
        instagram='instagram',
        linkedin='linkedin',
    )
    resp = client.get('/api/devkorner-infos/')
    assert resp.status_code == 200
    assert resp.data[0]['name'] == devkorner_infos.name
