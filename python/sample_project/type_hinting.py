<<<<<<< HEAD
<<<<<<< HEAD
from typing import TypeVar, Iterable, DefaultDict, Callable, Tuple, Dict, List
from collections import defaultdict


def send_mail(to: Union[str, Iterable[str]], 
              subject: str, 
              message: str, 
              bcc: Union[Optional[Iterable[str]], str]) -> None:
    """Sends email `message` to user or users `to` with specified `subject` and optional hidden email(s) `bcc`."""
    return None
=======
from typing import Iterable, Callable


def send_mail(to: list[dict[tuple[str, int]], str], subject: str, message: str, bcc: list[dict[tuple[str, int]], str]) -> str:
    """Sends email `message` to user or users `to` with specified `subject` and optional hidden email(s) `bcc`."""
    print(send_mail.__doc__)
    #pass


#help(Iterable)
help(Callable)
>>>>>>> 13169b790d1e6eb111d61bfee50f188c3ab02ea7
=======
<<<<<<< HEAD
from typing import TypeVar, Iterable, DefaultDict, Callable, Tuple, Dict, List
from collections import defaultdict


def send_mail(to: Union[str, Iterable[str]], 
              subject: str, 
              message: str, 
              bcc: Union[Optional[Iterable[str]], str]) -> None:
    """Sends email `message` to user or users `to` with specified `subject` and optional hidden email(s) `bcc`."""
    return None
=======
from typing import Iterable, Callable


def send_mail(to: list[dict[tuple[str, int]], str], subject: str, message: str, bcc: list[dict[tuple[str, int]], str]) -> str:
    """Sends email `message` to user or users `to` with specified `subject` and optional hidden email(s) `bcc`."""
    print(send_mail.__doc__)
    #pass


#help(Iterable)
help(Callable)
>>>>>>> 13169b790d1e6eb111d61bfee50f188c3ab02ea7
>>>>>>> refs/remotes/origin/readme
