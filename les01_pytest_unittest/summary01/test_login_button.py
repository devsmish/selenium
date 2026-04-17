import pytest
from les01_pytest_unittest.summary01.login_button import LoginButton


@pytest.fixture
def login_button():
    return LoginButton()


def test_button_has_correct_label(login_button):
    assert login_button.get_label() == "Login"

def test_button_is_enabled_by_standard(login_button):
    assert login_button.is_enabled() is True

def test_button_is_disabled_by_standard(login_button):
    login_button.disable()
    assert login_button.is_enabled() is False

def test_button_state_is_changing(login_button):
    login_button.disable()
    login_button.enable()
    assert login_button.is_enabled() is True
