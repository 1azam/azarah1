from telethon.tl.types import Chat, Channel, InputChannel
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest
from opentele.tl import TelegramClient
from telethon import TelegramClient
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError


async def add_user(client: TelegramClient, chat_instance, user_instance, fwd_limit: int = 100):
    # fwd_limit allows the user to see the number of last messages (in chats only!)
    # user_instance and chat_instance can be link or user or short name

    chat = await client.get_entity(chat_instance)

    if isinstance(chat, Chat):
        request = AddChatUserRequest(
            chat_id=chat.id,
            user_id=user_instance,
            fwd_limit=fwd_limit)

    elif isinstance(chat, Channel):
        request = InviteToChannelRequest(
            InputChannel(chat.id, chat.access_hash),
            [user_instance])

    else:
        return {'added': False, 'error': 'Chat argument is not a chat'}

    try:
        await client(request)
    except UserAlreadyParticipantError:
        return {'added': False, 'user_already_exists': True, 'error': 'User already exists in the chat'}
    except Exception as e:
        return {'added': False, 'user_already_exists': False, 'error': e.args[0]}

    return {'added': True, 'error': ''}
