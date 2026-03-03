from ..mon_app.main_app import add_bonus

def test_add_bonus():
    # Arrange & Act
    result = add_bonus(10.0)
    assert result == 12.0
