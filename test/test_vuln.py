import vulnerable_app

def test_calc_user_expression():
    assert vulnerable_app.calc_user_expression("1 + 1") == 2

def test_weak_hash():
    output = vulnerable_app.weak_hash("hello")
    assert isinstance(output, str)

def test_insecure_token():
    token = vulnerable_app.insecure_token()
    assert len(token) == 6
