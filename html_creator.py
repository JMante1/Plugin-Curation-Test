import os
import json

cwd = os.getcwd()
filename = os.path.join(cwd, "test.json")

with open(filename, 'r') as jsonfile:
    json_stuff = json.load(jsonfile)


submit_link = json_stuff['submit_link']


json_dict = json_stuff['interface']

html = f'<html>\n<body>\n<form action="{submit_link}" method="POST">'
html_end = '\n<input type="submit" value="Submit">\n\n</form>\n</body>\n</html>'

for variable in json_dict:
    default = variable['default']
    description = variable['description']
    label = variable['label']
    options = variable['options']
    type = variable['type']
    restrictions = variable['restrictions']
    id = label

    html += f'\n<h2>{label}</h2>\n'
    html += f'<p>{description}</p>\n'

    rest_str = ""
    if len(restrictions) > 0:
        for val in restrictions:
            rest_str += f' {val}="{restrictions[val]}"'


    if len(options) == 0:
        if len(default) > 0:
            def_str = f' value="{default[0]}"'
        else:
            def_str = ""
        html += f'<input type="{type}" id="{id}" name="{id}"{def_str}{rest_str}><br><br>\n'
    else:
        for ind, val in enumerate(options):
            # checked="checked"
            if val in default:
                def_str = ' checked="checked"'
            else:
                def_str = ''
            html += f'<input type="{type}" id="{val}" value="{val}" name="{id}"{def_str}>\n'
            html += f'<label for="{val}">{val}</label><br>\n'

html += html_end

with open(os.path.join(cwd, 'out.html'), 'w') as f:
    f.write(html)
# print(html)