# Telegram download Instagram posts

## Send a post link to telegram bot and receive images as media group


## Dev setup:

1. install poetry (globally or being inside the environment):
```shell
python3 -m pip install poetry
# or (being in env)
pip install poetry
```

2. Install packages
```shell
poetry install
```

3. setup venv in PyCharm (if not created automatically).
   To get info about env created by poetry run
```shell
poetry env info
```

4. setup pre-commit git hooks
```shell
pre-commit install
```

5. Copy env config:
```shell
# if running in docker (TODO)
cp .env.template .env.local.docker
# if running on local
cp .env.template .env.local
```

6. Add editor / IDE integration for black formatter
https://black.readthedocs.io/en/stable/integrations/editors.html


## Tips:

- Add dev dependencies
```shell
poetry add -D install pre-commit
```

-  Run `pre-commit` against all the files
```shell
pre-commit run --all-files
```

- Install a pre-prelease package:
```shell
poetry add --allow-prereleases "aioredis>=2.0.0b1"
```

- Install a pre-prelease package with extras:
```shell
poetry add --allow-prereleases "aioredis[hiredis]>=2.0.0b1"
```
