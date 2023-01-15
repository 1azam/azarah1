from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest


async def add_bots_to_chat(link, accounts):
    for account in accounts:
        if link.count('/+') != 0:
            link1 = link[link.find("+") + 1:]
            await account(ImportChatInviteRequest(link1))
        else:
            await account(JoinChannelRequest(link))


async def add_chat_to_db(link, chats, accounts):
    users = []

    if link.count('/+') != 0:
        link1 = link[link.find("+") + 1:]
        await accounts[0](ImportChatInviteRequest(link1))
    else:
        await accounts[0](JoinChannelRequest(link))

    chat = await accounts[0].get_entity(link)

    all_participants = await accounts[0].get_participants(chat, aggressive=True)

    for i in all_participants:
        if i.username:
            users.append(i.username)

    chats.insert_one({'name': chat.title, 'link': link, 'users': users[1:]})
