
from sim_kingdom import simulate


def test_produce():
    resources = {
        'wood': 0,
        'stone': 0,
        'mana': 0,

        'lumber mills': 0,
        'quarries': 0,
        'mage towers': 0,
    }
    result = simulate(resources, build='lumber mill')
    assert result['wood'] == 1
