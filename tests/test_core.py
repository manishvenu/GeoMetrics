import geometrics
import pytest


@pytest.mark.core
def test_import():
    assert geometrics.plot_tools is not None
