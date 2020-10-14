import json

import pytest

from devk.models import Team


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
def test_add_team_invalid_json(client):
    team = Team.objects.all()
    assert len(team) == 0

    resp = client.post(
        '/api/team/',
        {},
        content_type='application/json'
    )
    assert resp.status_code == 400

    team = Team.objects.all()
    assert len(team) == 0


@pytest.mark.django_db
def test_add_team_invalid_json_keys(client):
    team = Team.objects.all()
    assert len(team) == 0

    resp = client.post(
        '/api/team/',
        {
            'name': 'Abdoul BAH',
            'position': 'Full Stack Engineer',
        },
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
