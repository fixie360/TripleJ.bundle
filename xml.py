from xml.dom import minidom
xmldoc = minidom.parse('http://www.abc.net.au/triplej/feeds/playout/triplej_sydney_playout.xml')
itemlist = xmldoc.getElementsByTagName('item')
print(len(itemlist))
print(itemlist[0].attributes['name'].value)
for s in itemlist:
    print(s.attributes['name'].value)
