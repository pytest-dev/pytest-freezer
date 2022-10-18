import pytest
import freezegun


@pytest.fixture
def freezer(request):
    """Freeze time by mocking the datetime module"""
    marker = request.node.get_closest_marker("freeze_time")
    if marker:
        args = marker.args
        kwargs = marker.kwargs
    else:
        args = ()
        kwargs = {}
    freezer = freezegun.freeze_time(*args, **kwargs)
    try:
        yield freezer.start()
    finally:
        freezer.stop()


def pytest_collection_modifyitems(items):
    for item in items:
        if item.get_closest_marker("freeze_time"):
            item.fixturenames.insert(0, "freezer")


def pytest_configure(config):
    config.addinivalue_line("markers", "freeze_time(...): use freezegun to freeze time")
