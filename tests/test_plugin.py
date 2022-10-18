def test_freezer_move_to_method(pytester):
    pytester.makepyfile("""\
        from datetime import datetime

        def test_freezer_move_to_method(freezer):
            freezer.move_to("2021-01-01")
            assert datetime.now().year == 2021
            freezer.move_to("2022-01-01")
            assert datetime.now().year == 2022
    """)
    pytester.runpytest().assert_outcomes(passed=1)


def test_mark_decorator(pytester):
    pytester.makepyfile("""\
        import pytest
        from datetime import datetime
        
        @pytest.mark.freeze_time("2022-10-17T12:34:56")
        def test_mark_decorator():
            assert datetime.now().isoformat() == "2022-10-17T12:34:56"
    """)
    pytester.runpytest().assert_outcomes(passed=1)


def test_frozen_by_default_with_fixture(pytester):
    pytester.makepyfile("""\
        from datetime import datetime

        def test_frozen_by_default_with_fixture(freezer):
            dt1 = datetime.now()
            dt2 = datetime.now()
            assert dt1 == dt2
    """)
    pytester.runpytest().assert_outcomes(passed=1)


def test_not_frozen_with_no_fixture(pytester):
    pytester.makepyfile("""\
        from datetime import datetime

        def test_not_frozen_with_no_fixture():
            dt1 = datetime.now()
            dt2 = datetime.now()
            assert dt1 < dt2
    """)
    pytester.runpytest().assert_outcomes(passed=1)


def test_tick_method(pytester):
    pytester.makepyfile("""\
        from datetime import datetime
        
        def test_tick_method(freezer):
            freezer.move_to("2022-10-17")
            assert datetime.now() == datetime(2022, 10, 17)
            freezer.tick()
            assert datetime.now() == datetime(2022, 10, 17, 0, 0, 1)
            freezer.tick(delta=12)
            assert datetime.now() == datetime(2022, 10, 17, 0, 0, 13)
    """)
    pytester.runpytest().assert_outcomes(passed=1)
