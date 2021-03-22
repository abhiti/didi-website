from os import listdir
pics = listdir('./')
# print(pics)

# pics.sort()

uniquePrefixes = set()
orderedPics = {}
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for pic in pics:
    if ".jpg" not in pic:
        continue
    firstNumericalIndex = len(pic)
    for c in range(len(pic)):
        if pic[c] in digits:
            firstNumericalIndex = c
            break
    prefix = pic[:firstNumericalIndex]
    uniquePrefixes.add(prefix)
    if prefix not in orderedPics:
        orderedPics[prefix] = []
    # print("\nPREFIX",prefix,"\n\n")
    # print("HERE",pic[firstNumericalIndex:pic.index('.')])
    orderedPics[prefix].append(int(pic[firstNumericalIndex:pic.index('.')]))

# print("\n\n",orderedPics,"\n\n")

prefixOrder = ["bt", "gt"]

picsHtml = ""
for prefix in prefixOrder:
    pics = orderedPics[prefix]
    pics.sort()
    for pic in pics:
        # <img src="https://arts.columbia.edu/sites/arts.columbia.edu/files/thea_hs_vaish_kanika.jpg">
        picsHtml += '<img src="./gallery-images/directing/'+prefix+str(pic)+'.jpg">\n'
print(picsHtml)
