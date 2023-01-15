def get_chats_from_db(chats):
    stri = ''
    for chat in chats.find():
        stri += chat['name'] + ': ' + chat['link'] + '\nКоличество пользователей: ' + str(len(chat['users'])) + '\n' + '\n'
    if stri:
        return stri
    else:
        return "Пусто"