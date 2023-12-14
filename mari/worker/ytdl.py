import logging
from typing import List, Optional, Tuple

from yt_dlp.extractor import gen_extractor_classes, get_info_extractor

# from yt_dlp.extractor.common import UnsupportedURLIE
from yt_dlp.extractor.extractors import GenericIE
from yt_dlp.YoutubeDL import YoutubeDL  # noqa: F401

log = logging.getLogger(__name__)


def check_compatibility(
    url: str, enabled_extractors: Optional[List[str]] = None
) -> Tuple[bool, str]:
    """Can yt-dlp handle this URL?

    Parses through the InfoExtractors and attempt to match our URL against
    those valid for given extractors. Once the extractor is found, return
    status and listed extractor.
    """
    if enabled_extractors:
        extractors = [get_info_extractor(x) for x in enabled_extractors]
    else:
        extractors = gen_extractor_classes()

    for extractor in extractors:
        if enabled_extractors and not extractor._ENABLED:  # pragma: no cover
            log.debug("Skipping non-specified, non-enabled extractor: %s", extractor.IE_NAME)
            continue

        if extractor is GenericIE:
            log.debug("Skipping %s as it matches GenericIE", extractor.IE_NAME)
            continue

        if extractor.suitable(url):
            return (True, extractor.IE_NAME)

    return (False, None)
