from game import dice


def test_dice_should_return_a_dice():
    result = dice.dice()
    assert result == "dice", "dice must equal dice"
