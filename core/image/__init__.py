from dataclasses import dataclass, field
from typing import Callable, List

from alloff_backoffice_server.settings import DEFAULT_CACHING_SETTINGS, CachingSettings
from core.image.resize_and_cache_image import resize_and_cache
from core.image.url_filters import is_undownloadable

UrlNotFilter = Callable[[str], bool]


@dataclass
class BackofficeImageCacher:
    """
    BackofficeImageCacher class
    """

    raw_url: str
    caching_settings: CachingSettings = field(
        default_factory=lambda: DEFAULT_CACHING_SETTINGS
    )
    not_filters: List[UrlNotFilter] = field(default_factory=list)

    @property
    def resized_url(self) -> str:
        """
        Currently only supports max_width
        """
        if not self.is_cachable:
            return self.raw_url

        return resize_and_cache(
            self.raw_url,
            self.caching_settings["SIZE"],
            self.caching_settings["SUFFIX"],
        )

    @property
    def is_cachable(self) -> bool:
        """
        Tests against the not_filters to determine if the image is cachable.
        """
        for not_filter in [is_undownloadable, *self.not_filters]:
            if not_filter(self.raw_url):
                return False
        return True
