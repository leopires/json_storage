class _BasicError(Exception):

    def __init__(self, error_description: str, error_code: int = 0) -> None:
        super().__init__(f"({error_code}): {error_description}")
        self._error_description = error_description
        self._error_code = error_code

    @property
    def description(self) -> str:
        return self._error_description

    @property
    def code(self) -> int:
        return self._error_code

    def __repr__(self):
        return f"[{self.__class__.__name__}]: {self.code}, {self.description}"

    def __str__(self):
        return f"{self.code}, {self.description}"


class InvalidJsonStorage(_BasicError):
    def __init__(self, invalid_file_path: str) -> None:
        super().__init__(error_description=f"Invalid file '{invalid_file_path}'. It is not in JSON format.")
