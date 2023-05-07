from .start import dp
from .help import dp
from .phone import dp
from .counter import dp
from .zero_counter import dp
from .new_user import dp
# from .name import dp





# жадный хандлер в самый низ, что бы не перехватывал остальные сообщения
from .empty import dp

__all__ = ['dp']
