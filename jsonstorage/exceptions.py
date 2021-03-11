"""This modules has the exceptions raised by jsonstorage library.

"""


class _BasicError(Exception):
    """This class represents one basic error and encapsulate some code to display error messages.

    Properties
    ----------
    description : str
        The error description.
    code : int
        The error code.

    """

    def __init__(self, error_description: str, error_code: int = 0) -> None:
        super().__init__(f"({error_code}): {error_description}")
        self._error_description = error_description
        self._error_code = error_code

    @property
    def description(self) -> str:
        """This property returns the description of the error.

        :return: The error description.
        :rtype: str
        """
        return self._error_description

    @property
    def code(self) -> int:
        """This property returns the code of the error.

        :return: The error code.
        :rtype: int
        """
        return self._error_code

    def __repr__(self):
        return f"[{self.__class__.__name__}]: {self.code}, {self.description}"

    def __str__(self):
        return f"{self.code}, {self.description}"


class InvalidJsonStorage(_BasicError):
    """This exception occurs when the content of a given file is not in JSON format.

    """

    def __init__(self, invalid_file_path: str) -> None:
        super().__init__(error_description=f"Invalid file '{invalid_file_path}'. "
                                           f"It is not in JSON format.")
