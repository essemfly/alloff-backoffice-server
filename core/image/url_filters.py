from alloff_backoffice_server.settings import DO_NOT_CACHE_IMAGES_TO_S3_HOSTS


def is_undownloadable(url: str) -> bool:
    for host in DO_NOT_CACHE_IMAGES_TO_S3_HOSTS:
        if host in url:
            # If host is a no-go, return True.
            return True
    return False
