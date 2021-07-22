import pyperclip, re
newSlotNameNormal = "Dogtown: Miami Un-leashed 2.3, :Remix 2 34$" # input('enter new slot complete name, (eg: "Dogtown: Miami Un-leashed Remix"):...')
newSlotNameNoSymbols = re.sub(r'[^\w]', ' ', newSlotNameNormal)
newSlotNameNoSpace = newSlotNameNoSymbols.replace(' ', '')



"""newSlotNameNoSpace = newSlotNameNormal.replace(' ', '')
if '-' in newSlotNameNoSpace:
    newSlotNameNoSpace = newSlotNameNoSpace.replace('-', '')"""



print(newSlotNameNormal)
print(newSlotNameNoSymbols)
print(newSlotNameNoSpace)


"""doc = open('teaserAndLaunch.txt', 'r')
text = doc.read()
print('text______________________________________________________________\n', text)
newText = text.replace('MoMummy', 'NewSlot')
print('newText_____________________________________________________________________________\n', newText)"""

