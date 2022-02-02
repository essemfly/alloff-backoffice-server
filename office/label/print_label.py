import requests

from alloff_backoffice_server.settings import LABEL_SERVER_URL


def print_label(label_xml: str):
    print(label_xml)
    # requests.post(LABEL_SERVER_URL,
    #               data=label_xml.encode('utf-8'),
    #               headers={'Content-type': 'text/plain; charset=utf-8'}
    #               )
