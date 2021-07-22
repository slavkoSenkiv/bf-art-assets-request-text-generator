import pyperclip, re, pyinputplus
from pathlib import Path

"""def replacer(thing_to_replace, old_text, new_text):
    if thing_to_replace != '-':
        file_content = file_content.replace(old_text, new_text)
    if thing_to_replace == '-':
        file_content = file_content.replace(old_text, 'TBD')"""


def renamer(asset, new_name, id_non_vip, id_vip, id_hr, theme):

    new_name_no_symbols = re.sub(r'[^\w]', ' ', new_name)
    new_name_no_space = new_name_no_symbols.replace(' ', '')

    file_path = Path.cwd()/f'{asset}.txt'
    file = open(file_path, 'r')
    file_content = file.read()

    if new_name_no_space != '-':
        file_content = file_content.replace('MoMummy', new_name_no_space)
    if new_name_no_space == '-':
        file_content = file_content.replace('MoMummy', 'TBD')

    if new_name != '-':
        file_content = file_content.replace('Mo Mummy', new_name)
    if new_name == '-':
        file_content = file_content.replace('Mo Mummy', 'TBD')

    if id_non_vip != '-':
        file_content = file_content.replace('id_non_vip', id_non_vip)
    if id_non_vip == '-':
        file_content = file_content.replace('id_non_vip', 'TBD')

    if id_vip != '-':
        file_content = file_content.replace('id_vip', id_vip)
    if id_vip == '-':
        file_content = file_content.replace('id_vip', 'TBD')

    if id_hr != '-':
        file_content = file_content.replace('id_hr', id_hr)
    if id_hr == '-':
        file_content = file_content.replace('id_hr', 'TBD')

    if theme != '-':
        file_content = file_content.replace('momummy', theme)
    if theme == '-':
        file_content = file_content.replace('momummy', 'TBD')

    pyperclip.copy(file_content)

    print(file_content)


newSlotNameNormal = "Dog-town: Miami Un-leashed Remix"
buyInIdNonViP = '111'
buyInIdViP = '222'
buyInIdHR = '333'
theme = '-'

"""newSlotNameNormal = input('Enter new SLOT NAME, eg "Dog-town: Miami Un-leashed Remix", or "-" for tbd:...\n')
buyInIdNonViP = input('Enter new buy-in id for  nonVIP  , or "-" for tbd:...\n')
buyInIdViP = input('Enter new buy-in id for VIP, or "-" for tbd:...\n')
buyInIdHR = input('Enter new buy-in id for HR, or "-" for tbd:...\n')
theme = input('Enter new new Theme Name, or "-" for tbd:...\n')"""

while True:
    doc = pyinputplus.inputMenu(['teaser+launch',
                                 'jpSurge',
                                 'sales',
                                 'ejp',
                                 'offer'], 'pick asset u want copy to clipboard:\n', numbered=True)

    renamer(doc, newSlotNameNormal, buyInIdNonViP, buyInIdViP, buyInIdHR, theme)






