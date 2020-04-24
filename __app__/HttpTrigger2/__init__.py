"""An example Azure Function triggered by an HTTP get or post."""
import logging
import azure.functions as func
from __app__.sharedcode import my_helper_function


def main(req: func.HttpRequest) -> func.HttpResponse:
    """Deal with HttpTrigger1 event."""
    logging.info("Python HTTP trigger function processed a request.")
    logging.info(f"Run shared code function {my_helper_function.hello()}")

    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except AttributeError:
            pass
        else:
            name = req_body.get("name")

    if name:
        return func.HttpResponse(f"V2 Hello {name}!")
    else:
        return func.HttpResponse(
            "Please pass a name on the query string or in the request body",
            status_code=400,
        )
