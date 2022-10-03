from valorant import battle_pass


def test_parse_args():
    assert isinstance(battle_pass(50), int)
