[![actions](https://github.com/pytest-dev/pytest-freezer/actions/workflows/tests.yml/badge.svg)](https://github.com/pytest-dev/pytest-freezer/actions/workflows/tests.yml/)
[![codecov](https://codecov.io/gh/pytest-dev/pytest-freezer/branch/main/graph/badge.svg)](https://codecov.io/gh/pytest-dev/pytest-freezer)
[![pypi](https://img.shields.io/pypi/v/pytest-freezer.svg)](https://pypi.org/project/pytest-freezer)
![womm](https://cdn.rawgit.com/nikku/works-on-my-machine/v0.2.0/badge.svg)

# pytest-freezer

[Pytest][1] plugin providing a fixture interface for [freezegun][2].

## Installation:

``` bash
$ python -m pip install pytest-freezer
```

## Usage:

The fixture name is `freezer`. It is a `freezegun.api.FrozenDateTimeFactory` instance,
so refer to upstream freezegun [usage][3] for the methods.

Time is frozen by default when the fixture is injected:

``` python
def test_frozen_date(freezer):
    now = datetime.now()
    time.sleep(1)
    later = datetime.now()
    assert now == later
```

Time can be controlled within a test by using methods on the fixture:

``` python
def test_freezer_methods(freezer):
    freezer.move_to("2022-10-17")
    assert datetime.now() == datetime(2022, 10, 17)
    freezer.tick()
    assert datetime.now() == datetime(2022, 10, 17, 0, 0, 1)
    freezer.tick(delta=12)
    assert datetime.now() == datetime(2022, 10, 17, 0, 0, 13)
```

## Acknowledgements:

Credit to Tomasz Kontusz for the original [pytest-freezegun][4] plugin.

[1]: https://docs.pytest.org/
[2]: https://github.com/spulec/freezegun
[3]: https://github.com/spulec/freezegun#usage
[4]: https://github.com/ktosiek/pytest-freezegun
