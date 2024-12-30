import pytest


@pytest.mark.flaky(reruns=0)
@pytest.mark.usefixtures("setup", "log_on_failure")
class BaseTest:
    pass

