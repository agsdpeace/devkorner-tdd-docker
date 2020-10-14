import pytest

from devk.models import Team


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
