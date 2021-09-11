import xml.etree.ElementTree as ET

tree = ET.parse(open(filename))

repository = tree.getroot()

compoundname = repository.find('compounddef')

classes = {}

symbols = {}

for sectiondef in compoundname.findall('sectiondef'):
    for memberdef in sectiondef.findall('memberdef'):
        name = memberdef.find('name').text
        if memberdef.attrib['static'] == 'yes': # you can put static in interface, but should at least leave them static
            continue
        
        if memberdef.attrib['kind'] == "function":
            const = memberdef.attrib['const'] == 'yes'
            definition = memberdef.find('definition').text.split()
            return_type = memberdef.find('type').text
            arguments = memberdef.find('argsstring').text
            nargs = 0
            if arguments != '()':
                nargs = len(argsstring.split(','))
                
            print(f"virtual {return_type} {name}{arguments} = 0;")
