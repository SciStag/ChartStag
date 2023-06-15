"""
Tests the mermaid basic functionality
"""

import hashlib

from chartstag.mermaid import get_mermaid_version, get_mermaid_script


def test_version():
    assert get_mermaid_version() == "9.3.0"


def test_script():
    script_data = get_mermaid_script()
    assert len(script_data) == 2886654
    assert hashlib.md5(script_data).hexdigest() == "64684ea52f2f27acaea3da510b42f487"
