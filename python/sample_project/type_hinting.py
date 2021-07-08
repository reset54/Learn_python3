from typing import TypeVar, Iterable, DefaultDict, Callable, Tuple, Dict, List
from collections import defaultdict


def send_mail(to: Union[str, Iterable[str]], 
              subject: str, 
              message: str, 
              bcc: Union[Optional[Iterable[str]], str]) -> None:
    """Sends email `message` to user or users `to` with specified `subject` and optional hidden email(s) `bcc`."""
    return None