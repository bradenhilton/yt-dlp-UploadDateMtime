# Superseded by [yt-dlp-FixupMtime](https://github.com/bradenhilton/yt-dlp-FixupMtime)

### yt-dlp-UploadDateMtime

A [yt-dlp](https://github.com/yt-dlp/yt-dlp) postprocessor [plugin](https://github.com/yt-dlp/yt-dlp#plugins) which sets the file mtime to the upload date.

#### Installation

Requires yt-dlp `2023.01.02` or above.

You can install this package with pip:

```console
python3 -m pip install -U https://github.com/bradenhilton/yt-dlp-UploadDateMtime/archive/master.zip
```

See [installing yt-dlp plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins) for the other methods this plugin package can be installed.

#### Usage

Pass `--use-postprocessor UploadDateMtime` to activate the postprocessor.
