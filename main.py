import qrcode

text = input(("Text: "))
img = qrcode.make(text)

name = input("Введите название файла: ")
img.save(name + ".png")