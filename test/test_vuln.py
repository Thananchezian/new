import vulnerable_app

def test_calc():
    assert vulnerable_app.calculate("2 + 3") == 5
