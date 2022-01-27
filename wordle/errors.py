
class WordleException(Exception):
    """
    Base class for all wordle exception.
    """

class NotFound(WordleException):
    """
    The word was not found in the word list.
    """

class SizeNotAppropriate(WordleException):
    """
    The word does not contain the same size as the selected word.
    """

class MaxAttemptExceeded(WordleException):
    """
    The word does not contain the ruled letters.
    """