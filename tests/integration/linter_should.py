import os

import pep8
from expects import equal, expect
from tests.mamba_reserved_words import description, it

CHECKED_DIRS = ['commands', 'domain_events', 'domain', 'tests']


def root_path():
    this_path = os.path.normpath(os.path.dirname(__file__))
    return os.path.abspath(os.path.join(this_path, os.pardir, os.pardir))


def get_config_file():
    return os.path.join(root_path(), 'linter.cfg')


with description('Test Code Conformation'):
    with it('conforms PEP8'):
        pep8style = pep8.StyleGuide(config_file=get_config_file())
        result = pep8style.check_files(CHECKED_DIRS)
        expect(result.total_errors).to(equal(0))
