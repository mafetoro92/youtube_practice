import gspread
from oauth2client.service_account import ServiceAccountCredentials
import typing
import config


def insert_row_col(info_sheet: typing.List[typing.Dict[str, str]]) -> typing.List[list]:
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(config.GOOGLE_CREDENTIALS, scope)
    client = gspread.authorize(creds)
    sheet = client.open(config.GOOGLE_SHEET_NAME)
    worksheet2 = sheet.worksheet('Sheet2')

    header = ['likes', 'upload_date', 'url']

    sheet_values = {}

    for d in info_sheet:
        for k in d:
            if k not in sheet_values:
                sheet_values[k] = [d[k]]
            else:
                sheet_values[k].append(d[k])

    # create list of lists
    key=[list(sheet_values.keys())]
    value=list(sheet_values.values())


    v = []
    v.append(list(sheet_values.values()))

    t=[]
    for m in v:
        for n in m:
            v1=n[0]
            t.append(v1)
            v2=n[1]
            t.append(v2)
            v3=n[2]
            t.append(v3)

    l = []
    l.append(header)
    a = info_sheet[0]
    b = info_sheet[1]
    c = info_sheet[2]
    add_info_a = []
    add_info_b = []
    add_info_c = []

    for row in a.values():
        add_info_a.append(row)

    for x in b.values():
        add_info_b.append(x)

    for m in c.values():
        add_info_c.append(m)

    t = []
    t.append(add_info_a)
    t.append(add_info_b)
    t.append(add_info_c)

    for e in t:
        l.append(e)

    worksheet2.update(l)
    return t
