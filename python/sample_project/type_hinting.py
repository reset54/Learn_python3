from typing import Iterable, Callable


def send_mail(to: list[dict[tuple[str, int]], str], subject: str, message: str, bcc: list[dict[tuple[str, int]], str]) -> str:
    """Sends email `message` to user or users `to` with specified `subject` and optional hidden email(s) `bcc`."""
    print(send_mail.__doc__)
    #pass


#help(Iterable)
help(Callable)