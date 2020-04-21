# tests/test_httptrigger.py
import pytest

import azure.functions as func
from __app__.HttpTrigger1 import main


def test_main():
    # Construct a mock HTTP request.
    req = func.HttpRequest(
        method="POST", body=None, url="/api/HttpTrigger1", params={"name": "Test"}
    )

    # Call the function.
    resp = main(req)

    # Check the output.
    assert resp.get_body() == b"Hello Test!"
