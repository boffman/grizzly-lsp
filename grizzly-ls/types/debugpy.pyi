import typing

Endpoint = typing.Tuple[str, int]

def listen(__endpoint: Endpoint | int, *, in_process_debug_adapter: bool = False) -> Endpoint: ...
def wait_for_client() -> None: ...
