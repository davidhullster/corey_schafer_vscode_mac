import pytest
import script

def test_setup():
    assert "Hello Test" == script.greet("Test")
