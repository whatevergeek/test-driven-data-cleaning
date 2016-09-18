import os
import subprocess
import pytest

from tddc import build


@pytest.fixture()
def build_class(fixtures_dir, input_filename, tmpdir):
    return build.Scripts(
        summaries_root_dir=fixtures_dir,
        input_file=input_filename,
        scripts_root_dir=tmpdir.strpath,
        output_dir='')


def is_same_file(file_a, file_b):
    diff_return = subprocess.call(['diff', file_a, file_b])
    return diff_return == 0


def test_write_cleaning_script(build_class, fixtures_dir, input_filename):
    cleaning_file = build_class.write_cleaning_script()
    fixture_clean = os.path.join(
        fixtures_dir, 'clean_' + os.path.splitext(input_filename)[0] + '.txt'
    )
    assert is_same_file(cleaning_file, fixture_clean)


def test_write_test_cleaning_script(build_class, fixtures_dir, input_filename):
    test_cleaning_file = build_class.write_test_cleaning_script()
    fixture_test_clean = os.path.join(
        fixtures_dir, 't_clean_' + os.path.splitext(input_filename)[0] + '.txt'
    )
    assert is_same_file(test_cleaning_file, fixture_test_clean)
