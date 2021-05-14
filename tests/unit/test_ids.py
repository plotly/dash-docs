import os
import re
import logging
import pytest
import sys

logger = logging.getLogger(__name__)

@pytest.mark.skipif(
    sys.version_info < (3, 7),
    reason="skip non-essential, potentially flaky tests"
)
def test_no_duplicate_ids():
    found_ids = {}
    root_dir = os.path.abspath(
        os.path.join(os.path.split(__file__)[0], '..', '..', 'dash_docs')
    )
    id_regex = re.compile(r'\Wid\s*[=:]\s*(\'([^\']*)\'|"([^"]*)")')
    cnt = 0
    for root, dir, files in os.walk(root_dir):
        for filename in files:
            if not filename.endswith('.py'):
                continue
            path = os.path.join(root, filename)
            cnt += 1
            with open(path) as f:
                file_ids = {}
                multiline_str = ''
                for line in f:
                    if line.count("'''") % 2 == 1:
                        if not multiline_str:
                            multiline_str = "'''"
                        elif multiline_str == "'''":
                            multiline_str = ''
                        continue
                    if line.count('"""') % 2 == 1:
                        if not multiline_str:
                            multiline_str = '"""'
                        elif multiline_str == '"""':
                            multiline_str = ''
                        continue
                    if multiline_str:
                        continue

                    if '# no-exec' in line or '# skip-id-check':
                        continue

                    matches = id_regex.findall(line)
                    for match in matches:
                        found_id = match[1] or match[2]
                        assert found_id not in found_ids, (
                            'found {} in both {} and {}'.format(
                                found_id, found_ids[found_id], path
                            )
                        )
                        file_ids[found_id] = path
                # allow duplicates within one file - sometimes that's intended,
                # if not we'd have caught it already
                found_ids.update(file_ids)
    logger.info('completed test_no_duplicate_ids, tested {} files'.format(cnt))
