import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import vulnerable_app

def test_calc():
    assert vulnerable_app.calculate("2 + 3") == 5
