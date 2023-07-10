import pandas_read_xml as pdx 

datframe = pdx.read_xml("data.xml")

print(datframe.to_json())



