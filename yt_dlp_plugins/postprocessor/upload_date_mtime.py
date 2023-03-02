from yt_dlp.postprocessor.common import PostProcessor
from yt_dlp.utils import datetime_from_str, hyphenate_date


class UploadDateMtimePP(PostProcessor):
    def __init__(self, downloader=None, **kwargs):
        super().__init__(downloader)
        self._kwargs = kwargs

    def run(self, info):
        upload_date = info.get('upload_date')
        if upload_date:
            self.to_screen(
                f'Setting {info["_filename"]!r} mtime to {hyphenate_date(upload_date)}')
            timestamp = datetime_from_str(upload_date).timestamp()
            self.try_utime(info['filepath'], timestamp, timestamp)
        return [], info
