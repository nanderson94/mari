import pytest


def test_import():
    from mari.worker import ytdl  # noqa: F401
    from mari.worker import gallery_dl  # noqa: F401


@pytest.mark.parametrize(
    "n,expected",
    [
        (("https://www.youtube.com/watch?v=M4gD1WSo5mA",), (True, "youtube")),
        (("https://yahoo.com/",), (False, None)),
        (("https://www.youtube.com/watch?v=M4gD1WSo5mA", ["TwitchVod"]), (False, None)),
        (("https://www.youtube.com/watch?v=M4gD1WSo5mA", ["Youtube"]), (True, "youtube")),
    ],
)
def test_ytdl_check_compatibility(n, expected):
    from mari.worker.ytdl import check_compatibility

    assert check_compatibility(*n) == expected


@pytest.mark.parametrize(
    "n,expected",
    [
        (("https://twitter.com/USER/tweets",), (True, "gallery_dl.extractor.twitter")),
        (("https://yahoo.com/",), (False, None)),
        (("https://twitter.com/USER/tweets", ["twitter"]), (True, "gallery_dl.extractor.twitter")),
        (
            ("https://twitter.com/USER/tweets", ["gallery_dl.extractor.twitter"]),
            (True, "gallery_dl.extractor.twitter"),
        ),
        (("https://twitter.com/USER/tweets", ["imgur"]), (False, None)),
        (("https://twitter.com/USER/tweets", ["moduledoesnotexist"]), (False, None)),
    ],
)
def test_gdl_check_compatibility(n, expected):
    from mari.worker.gallery_dl import check_compatibility

    assert check_compatibility(*n) == expected
