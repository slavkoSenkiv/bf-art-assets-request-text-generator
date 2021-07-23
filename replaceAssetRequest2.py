import pyperclip, re, pyinputplus
from pathlib import Path


def handler(doc_file, new_name, id_non_vip, id_vip, id_hr, theme_name):

    def replacer(new_text, old_text, doc_content):
        if new_text == '-':
            doc_content = doc_content.replace(old_text, 'TBD')
        else:
            doc_content = doc_content.replace(old_text, new_text)
        return doc_content

    new_name_no_symbols = re.sub(r'[^\w]', ' ', new_name)
    new_name_no_space = new_name_no_symbols.replace(' ', '')

    file_path = Path.cwd()/f'{doc_file}.txt'
    file = open(file_path, 'r')
    file_content = file.read()

    replacer(new_name_no_space, 'MoMummy', file_content)
    replacer(new_name, 'Mo Mummy', file_content)
    replacer(id_non_vip, 'id_non_vip', file_content)
    replacer(id_vip, 'id_non_vip', file_content)
    replacer(id_hr, 'id_hr', file_content)
    replacer(theme_name, 'momummy', file_content)

    pyperclip.copy(file_content)
    print(file_content)


newSlotNameNormal = "2 Dog-town: Miami Un-leashed Remix"
buyInIdNonVIP = '111'
buyInIdVIP = '222'
buyInIdHR = '333'
theme = '-'

while True:
    doc = pyinputplus.inputMenu(['teaser+launch',
                                 'jpSurge',
                                 'sales',
                                 'ejp',
                                 'offer'], 'pick asset u want copy to clipboard:\n', numbered=True)

    handler(doc, newSlotNameNormal, buyInIdNonVIP, buyInIdVIP, buyInIdHR, theme)






