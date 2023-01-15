import zipfile
from opentele.api import UseCurrentSession
from opentele.td import TDesktop


async def add_accounts_from_tdata(file, accounts):
    paths1 = []
    paths = []
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall()
        for folder in zip_ref.namelist():
            paths1.append(folder)
        zip_ref.close()
    for i in range(0, len(paths1), 9):
        paths.append(paths1[i])
    for path in paths:
        tdataFolder = './' + path + 'tdata'
        tdesk = TDesktop(tdataFolder)

        assert tdesk.isLoaded()

        client = await tdesk.ToTelethon(session=path, flag=UseCurrentSession)

        await client.connect()

        accounts.append(client)
