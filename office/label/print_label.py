import requests

from alloff_backoffice_server.settings import LABEL_SERVER_URL, SERVICE_ENV_IS_DEV


def print_label(label_xml: str):
    if SERVICE_ENV_IS_DEV:
        print(label_xml)
    else:
        requests.post(LABEL_SERVER_URL,
                    data=label_xml.encode('utf-8'),
                    headers={'Content-type': 'text/plain; charset=utf-8'}
                    )
