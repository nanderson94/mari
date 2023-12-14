import importlib
import logging
from typing import List, Optional, Tuple

from gallery_dl.extractor import add_module, extractors

log = logging.getLogger(__name__)


def check_compatibility(
    url: str, enabled_extractors: Optional[List[str]] = None
) -> Tuple[bool, str]:
    """Determine which gallery_dl extractor could be used for this content

    Runs the matcher for each enabled extractor (all by default) to determine
    which one, if any, can be used on the provided url.
    """
    if not enabled_extractors:
        exts = extractors()
    else:
        exts = []
        for extractor in enabled_extractors:
            if "." not in extractor:
                extractor = f"gallery_dl.extractor.{extractor}"
            try:
                extractor_module = importlib.import_module(extractor)
            except ImportError:
                print(f"Extractor invalid {extractor}")
                log.warn("Invalid extractor selected: %s", extractor)
                continue

            exts += add_module(extractor_module)

    for extractor in exts:
        if extractor.pattern.match(url):
            return (True, extractor.__module__)

    return (False, None)
