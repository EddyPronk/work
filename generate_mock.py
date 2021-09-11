import xml.etree.ElementTree as ET

tree = ET.parse(open(filename))

repository = tree.getroot()

compoundname = repository.find('compounddef')

classes = {}

symbols = {}

for sectiondef in compoundname.findall('sectiondef'):
    for memberdef in sectiondef.findall('memberdef'):
        name = memberdef.find('name').text
        if memberdef.attrib['kind'] == "function":
            const = memberdef.attrib['const'] == 'yes'
            definition = memberdef.find('definition').text.split()
            typenode = memberdef.find('type')
            ref = typenode.find('ref')
            if ref is not None:
                return_type = ref.text
            else:
                return_type = typenode.text
            argsstring = memberdef.find('argsstring').text
            arguments = argsstring[:argsstring.find(')') + 1]
            nargs = 0
            if arguments != '()':
                nargs = len(argsstring.split(','))
                
            if len(definition) == 2: # skip dtor
                continue

            if const:
                macro = f"MOCK_CONST_METHOD{nargs}"
            else:
                macro = f"MOCK_METHOD{nargs}"
                
            print(f"{macro}({name}, {return_type}{arguments});")
