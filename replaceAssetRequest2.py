import pyperclip, re, pyinputplus
from pathlib import Path


def replacer(new_text, old_text, doc_content):
    if new_text == None:
        doc_content = doc_content.replace(old_text, 'TBD')
    if new_text != None:
        doc_content = doc_content.replace(old_text, new_text)
    return doc_content


def handler(doc_file, new_name, id_non_vip, id_vip, id_hr, theme_name):

    new_name_no_symbols = re.sub(r'[^\w]', ' ', new_name)
    new_name_no_space = new_name_no_symbols.replace(' ', '')

    file_path = Path.cwd()/f'{doc_file}.txt'
    file = open(file_path, 'r')
    file_content = file.read()

    file_content = replacer(new_name_no_space, 'MoMummy', file_content)
    file_content = replacer(new_name, 'Mo Mummy', file_content)
    file_content = replacer(id_non_vip, 'id_non_vip', file_content)
    file_content = replacer(id_vip, 'id_non_vip', file_content)
    file_content = replacer(id_hr, 'id_hr', file_content)
    file_content = replacer(theme_name, 'momummy', file_content)

    pyperclip.copy(file_content)
    print(file_content)


def ask(thing):
    thing = input(f'enter {thing} or pres "enter" if TBD: ')
    return thing


newSlotNameNormal = ask('SLOT NAME')
buyInIdNonVIP = ask('ID for NON VIP')
buyInIdVIP = ask('ID for VIP')
buyInIdHR = ask('ID for HR')
theme = ask('THEME')

while True:
    doc = pyinputplus.inputMenu(['teaser+launch',
                                 'jpSurge',
                                 'sales',
                                 'ejp',
                                 'offer'], 'enter number to copy to clipboard:\n', numbered=True)

    handler(doc, newSlotNameNormal, buyInIdNonVIP, buyInIdVIP, buyInIdHR, theme)






