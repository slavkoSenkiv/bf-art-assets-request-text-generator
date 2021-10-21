import pyperclip, re, pyinputplus
from pathlib import Path

# <editor-fold desc="functions">
def ask(thing):
    thing = input(f'enter {thing} or pres "enter" if TBD: ')
    return thing


def add_multipliers(slot_name_no_symbols, multipliers):

    if multipliers[-1] == '': # in case someone can enter extra space in the end of multipliers input
        multipliers = multipliers[0:-1]

    sting1 = slot_name_no_symbols
    string2 = ''

    for i in multipliers:
        if multipliers.index(i) < len(multipliers) - 1:
            sting1 = sting1 + i + 'x | '
            string2 = string2 + i + 'X SALE! | '
        else:
            sting1 = sting1 + i + 'x'
            string2 = string2 + i + 'X SALE!'

    sting1 = sting1.replace('.', '')
    return sting1 + ' **\n' + string2


def replacer(new_text, old_text, doc_content):
    if new_text == '':
        doc_content = doc_content.replace(old_text, 'TBD')
    if new_text != '':
        doc_content = doc_content.replace(old_text, new_text)
    else:
        doc_content = doc_content.replace(old_text, 'TBD')
    return doc_content


def replacer_jp_name(new_text, old_text, new_slot_name_normal, doc_content):
    if new_text == 'jp':
        doc_content = doc_content.replace(old_text, f"Win 2x | 3x the Jackpot! (there aren't multiple jackpots in {new_slot_name_normal})")
    if new_text == '':
        doc_content = doc_content.replace(old_text, f"Win 2x | 3x the TBD Jackpot! (there [aren't/are] multiple jackpots in {new_slot_name_normal})")
    else:
        doc_content = doc_content.replace(old_text, f"Win 2x | 3x the {new_text}! (there are multiple jackpots in {new_slot_name_normal})")
    return doc_content


def handler(doc_file, new_name, buyInIds_BFC, buyInIds_JMS, theme_name):

    new_name_no_symbols = re.sub(r'[^\w]', ' ', new_name)
    new_name_no_space = new_name_no_symbols.replace(' ', '')

    file_path = Path.cwd()/f'{doc_file}.txt'
    file = open(file_path, 'r')
    file_content = file.read()

    file_content = replacer(new_name_no_space, 'MoMummy', file_content)
    file_content = replacer(new_name, 'Mo Mummy', file_content)
    file_content = replacer(theme_name, 'momummy', file_content)
    file_content = replacer(add_multipliers(new_name_no_space, saleMultipliersBFC), 'NameWithMultipliersBFC', file_content)
    file_content = replacer(add_multipliers(new_name_no_space, saleMultipliersJMS), 'NameWithMultipliersJMS', file_content)
    file_content = replacer_jp_name(largest_jp_name, 'largest_jp_name_here', newSlotNameNormal, file_content)

    try:
        file_content = replacer(str(buyInIds_BFC[0]), 'NonVIP_BuyInIDsBFC', file_content)
    except IndexError:
        file_content = replacer('TBD', 'NonVIP_BuyInIDsBFC', file_content)

    try:
        file_content = replacer(str(buyInIds_BFC[1]), 'VIP_BuyInIDsBFC', file_content)
    except IndexError:
        file_content = replacer('TBD', 'VIP_BuyInIDsBFC', file_content)

    try:
        file_content = replacer(str(buyInIds_BFC[2]), 'HR_BuyInIDsBFC', file_content)
    except IndexError:
        file_content = replacer('TBD', 'HR_BuyInIDsBFC', file_content)

    try:
        file_content = replacer(str(buyInIds_JMS[0]), 'NonVIP_BuyInIDsJMS', file_content)
    except IndexError:
        file_content = replacer('TBD', 'NonVIP_BuyInIDsJMS', file_content)

    try:
        file_content = replacer(str(buyInIds_JMS[1]), 'VIP_BuyInIDsJMS', file_content)
    except IndexError:
        file_content = replacer('TBD', 'VIP_BuyInIDsJMS', file_content)

    pyperclip.copy(file_content)
    print(file_content)
# </editor-fold>

# <editor-fold desc="ask input part">
newSlotNameNormal = ask('SLOT NAME')
saleMultipliersBFC = ask('BFC SALE MULTIPLIERS, separated by space, eg "5.5 1.25"').split(' ')
saleMultipliersJMS = ask('JMS SALE MULTIPLIERS, separated by space, eg "5.5 1.25"').split(' ')
buyInId_BFC = ask('BFC buy-in id nonVIP, VIP and HR IDs respectively, separated by space, eg "111 222 333", ').split(' ')
buyInId_JMS = ask('JMS buy-in id nonVIP, VIP IDs respectively, separated by space, eg "111 222", ').split(' ')
largest_jp_name = ask('the LARGEST JP NAME if there are few, "jp" if there is only 1, ')
theme = ask('SLOT THEME')
# </editor-fold>

while True:
    doc = pyinputplus.inputMenu(['teaser+launch',
                                 'jpSurge',
                                 'sales',
                                 'ejp',
                                 'offer'], '\n\nenter number to copy to clipboard:\n', numbered=True)

    handler(doc, newSlotNameNormal, buyInId_BFC, buyInId_JMS, theme)




