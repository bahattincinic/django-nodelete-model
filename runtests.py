#!/usr/bin/env python
import os
import sys
import django

if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'

    from django.conf import settings
    from django.test.utils import get_runner

    django.setup()
    os.chdir('tests')
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))
