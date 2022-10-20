import freezegun
import pytest


freezegun.configure(extend_ignore_list=["_pytest.terminal", "_pytest.runner"])


@pytest.fixture
def freezer(request):
    """Freeze time by mocking the datetime module"""
    marker = request.node.get_closest_marker("freeze_time")
    args = getattr(marker, "args", ())
    kwargs = getattr(marker, "kwargs", {})
    with freezegun.freeze_time(*args, **kwargs) as frozen_datetime_factory:
        yield frozen_datetime_factory


def pytest_collection_modifyitems(items):
    for item in items:
        if item.get_closest_marker("freeze_time"):
            item.fixturenames.insert(0, "freezer")


def pytest_configure(config):
    config.addinivalue_line("markers", "freeze_time(...): use freezegun to freeze time")
