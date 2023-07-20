import logging

from http import HTTPStatus

import logging
import azure.functions as func
import requests



def main(req: func.HttpRequest) -> func.HttpResponse:
    # logging.info('Python HTTP trigger function processed a request.')

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )

    # logging.info('Start at: %i', round(time.time() * 1000))

    try:

        # call testHT2 in same azure function app

        url = "https://sam-py-linux.azurewebsites.net/api/HttpTrigger1"

        response = requests.post( url, json={

            'name': 'sam'

        })

        logging.info(response.text)

        if response.status_code != 200:

            raise Exception(response.text)

    except Exception as e:

        logging.error(str(e))

        return func.HttpResponse(str(e), status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value)

    return func.HttpResponse(status_code=HTTPStatus.NO_CONTENT.value)