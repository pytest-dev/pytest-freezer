|actions|_ |codecov|_ |pypi|_ |womm|_

.. |actions| image:: https://github.com/pytest-dev/pytest-freezer/actions/workflows/tests.yml/badge.svg
.. _actions: https://github.com/pytest-dev/pytest-freezer/actions/workflows/tests.yml/

.. |codecov| image:: https://codecov.io/gh/pytest-dev/pytest-freezer/branch/main/graph/badge.svg
.. _codecov: https://codecov.io/gh/pytest-dev/pytest-freezer

.. |pypi| image:: https://img.shields.io/pypi/v/pytest-freezer.svg
.. _pypi: https://pypi.org/project/pytest-freezer

.. |womm| image:: https://cdn.rawgit.com/nikku/works-on-my-machine/v0.2.0/badge.svg
.. _womm: https://github.com/nikku/works-on-my-machine


pytest-freezer
==============

Pytest_ plugin providing a fixture interface for freezegun_.

Installation:
-------------

.. code-block:: bash

   $ python -m pip install pytest-freezer

Usage:
------

The fixture name is ``freezer``. It is a ``freezegun.api.FrozenDateTimeFactory`` instance, so refer to upstream freezegun usage_ for the methods.

Time is frozen by default when the fixture is injected:

.. code-block:: python

   def test_frozen_date(freezer):
       now = datetime.now()
       time.sleep(1)
       later = datetime.now()
       assert now == later

Time can be controlled within a test by using methods on the fixture:

.. code-block:: python

   def test_freezer_methods(freezer):
       freezer.move_to("2022-10-17")
       assert datetime.now() == datetime(2022, 10, 17)
       freezer.tick()
       assert datetime.now() == datetime(2022, 10, 17, 0, 0, 1)
       freezer.tick(delta=12)
       assert datetime.now() == datetime(2022, 10, 17, 0, 0, 13)

Acknowledgements:
-----------------

Credit to Tomasz Kontusz for the original pytest-freezegun_ plugin.

.. _Pytest: https://docs.pytest.org/
.. _freezegun: https://github.com/spulec/freezegun
.. _pytest-freezegun: https://github.com/ktosiek/pytest-freezegun
.. _usage: https://github.com/spulec/freezegun#usage
