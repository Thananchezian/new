import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import vulnerable_app

def test_calc_user_expression():
    assert vulnerable_app.calc_user_expression("2 + 3") == 5

def test_weak_hash():
    output = vulnerable_app.weak_hash("password")
    # MD5 hash of "password" is a string of length 32
    assert isinstance(output, str)
    assert len(output) == 32

def test_insecure_token():
    token = vulnerable_app.insecure_token()
    assert token.isdigit()
    assert len(token) == 6

def test_get_user_password_returns_none_for_nonexistent_user():
    # Safe: we pass a username that doesn't exist
    result = vulnerable_app.get_user_password(":memory:", "nonexistent")
    assert result is None
