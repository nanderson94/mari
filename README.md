# Mari

Mari is a content-aware, distributed archiving service.

Control service:
* Inspect jobs
* Monitor jobs
* Create jobs

Dispatcher:
* Continuously slices up discovered items to workers
* Tracks job success/failures for requeues

Worker:
* Accepts work from queue

Planned worker types:
* yt-dlp extractors
* Heritrix3

