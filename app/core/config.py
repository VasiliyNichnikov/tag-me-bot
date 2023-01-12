import json

from app.core.utils import get_config_path


class Tag:
    def __init__(self, tags: dict) -> None:
        self._all = tags["all"]
        self._lol = tags["lol"]

    @property
    def all(self):
        return self._all

    @property
    def lol(self):
        return self._lol


class Config:
    def __init__(self, data: dict) -> None:
        print(data)
        self._tag = Tag(data["tag"])

    @property
    def tag(self):
        return self._tag


__factory = None


def get_config() -> Config:
    global __factory

    if __factory is None:
        config_path = get_config_path()
        with open(config_path, 'r', encoding='utf-8') as rf:
            data = json.loads(rf.read())
            __factory = Config(data)

    return __factory
