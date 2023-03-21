
from sim_kingdom import simulate_month


def test_build_and_produce():
    resources = {
        'wood': 3,
        'stone': 0,
        'mana': 0,

        'lumber mills': 5,
        'quarries': 0,
        'mage towers': 0,
    }
    result = simulate_month(resources, 'lumber mill')
    assert result['wood'] == 9
    assert result['lumber mills'] == 6
