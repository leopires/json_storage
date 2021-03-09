import os
from json import dump, load, JSONDecodeError

from jsonstorage import InvalidJsonStorage


def _check_sting_value(value_name: str, value: str):
    if not value:
        raise ValueError(f"Invalid {value_name}. Can't be None or empty string.")


class JsonStorage:

    def __init__(self, path: str) -> None:
        _check_sting_value(value_name='file path', value=path)
        self._file_path = path
        if os.path.isfile(path=self._file_path):
            self._load_data()
        else:
            self._data = dict()

    def _load_data(self):
        with open(file=self._file_path, encoding='utf8', mode='r') as file:
            try:
                self._data = load(fp=file)
            except JSONDecodeError as json_file_error:
                raise InvalidJsonStorage(invalid_file_path=self._file_path) from json_file_error

    @property
    def data(self) -> dict:
        return self._data

    def set_value(self, key: str, value: object) -> None:
        _check_sting_value(value_name='key', value=key)
        key_tokens = key.split('.')
        entry = self.data
        while key_tokens:
            token = key_tokens.pop(0)
            if not entry and key_tokens:
                entry[token] = dict()
            elif not key_tokens:
                entry[token] = value
            entry = entry[token]

    def get_value(self, key: str):
        _check_sting_value(value_name='key', value=key)
        key_tokens = key.split('.')
        entry = self.data
        while key_tokens:
            token = key_tokens.pop(0)
            if entry is None:
                return None
            else:
                if isinstance(entry, dict):
                    try:
                        entry = entry[token]
                    except KeyError:
                        return None
                else:
                    return entry
        return entry

    def save(self, debug: bool = False):
        with open(file=self._file_path, encoding='utf8', mode='w') as file:
            indent = None
            if debug:
                indent = 2
            dump(obj=self.data, fp=file, indent=indent, ensure_ascii=False)

    def __repr__(self):
        return f"{self.data!s}"
