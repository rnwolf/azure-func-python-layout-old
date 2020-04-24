"""Test the HttpTrigger1 Azure function."""
# tests/test_HttpTrigger1.py

import azure.functions as func
from __app__.HttpTrigger1 import main


def test_func_for_user_names_via_params():
    """Construct a mock HTTP request."""
    req = func.HttpRequest(
        method="POST", body=None, url="/api/HttpTrigger1", params={"name": "Test"}
    )

    # Call the function.
    resp = main(req)

    # Check the output.
    assert resp.get_body() == b"Hello Test!"


def test_func_for_user_names_via_body():
    """Construct a mock HTTP request."""
    req = func.HttpRequest(
        method="POST", body=b'{"name":"Test"}', url="/api/HttpTrigger1", params={}
    )

    # Call the function.
    resp = main(req)

    # Check the output.
    assert resp.get_body() == b"Hello Test!"


def test_func_for_no_name():
    """Construct a mock HTTP request."""
    req = func.HttpRequest(method="POST", body=None, url="/api/HttpTrigger1", params={})

    # Call the function.
    resp = main(req)

    # Check the output.
    assert (
        resp.get_body()
        == b"Please pass a name on the query string or in the request body"
    )
