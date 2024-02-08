# cool-anime-cli
An anime cli that have 4 source url's.Made for linux,Would also work on windows and mac.

available sources:
- gogo-server-1
- gogo-server-2
- gogo-filelions-1
- gogo-streamwish-1

These sources are hard to deploy on web so i added these as CLI programs.

## USAGE
```
pip install -r requirements.txt
```
Required packages:

- requests
- cloudscraper [some sites use cloudflare]
- re
- questionary [TUI]
- `mpv` [As a system binary executable in the path/not pypi module]
```
python3 main.py
```

## Note
This is made as a proof of concept,using it must be at your own risk,and this has no warranty.

## Thanks
- Ciarands [for the `packed` extractor]
