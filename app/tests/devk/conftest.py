import pytest

from devk.models import Team


@pytest.fixture(scope='function')
def add_team():
    def _add_team(name, position, biography, linkedin, twitter):
        team = Team.objects.create(name=name, position=position, biography=biography, linkedin=linkedin, twitter=twitter)
        return team
    return _add_team
