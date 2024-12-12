import azure.functions as func
from utils import add
from multiplication.multiply import mul
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        a = req.params.get('a')
        b = req.params.get('b')
        if a and b:
            a = int(a)
            b = int(b)
            return func.HttpResponse(
                f"Sum is {add(a,b)} and multiply is {mul(a,b)}",
                status_code=200
            )
        return func.HttpResponse(
            f"Invalid params {a,b}",
            status_code=201
        )
    except ValueError:
        return func.HttpResponse(
            f"Invalid params for adding{a,b}",
            status_code=201
        )
