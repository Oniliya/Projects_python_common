from .start import dp
from .help import dp
from .phone import dp


# жадный хандлер в самый низ, что бы не перехватывал остальные сообщения
from .empty import dp


__all__ = ['dp']

