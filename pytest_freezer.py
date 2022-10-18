import pytest
import freezegun


@pytest.fixture
def freezer(request):
    marker = request.node.get_closest_marker("freeze_time")
    if marker:
        ignore = marker.kwargs.pop("ignore", [])
        args = marker.args
        kwargs = marker.kwargs
    else:
        args = ()
        kwargs = {}
        ignore = []
    ignore += "_pytest.terminal", "_pytest.runner"
    freezer = freezegun.freeze_time(*args, ignore=ignore, **kwargs)
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
