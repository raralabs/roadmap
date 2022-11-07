## Copyrights : Sushan Shakya

## Use this script to generate snippet for contributors

import json

filename = "contributors.json"
output_filename = "contributors.md"


title_template = '> {}'

base_template = '''
<table>
<tr>
{}
</tr>
</table>
'''

user_template = '''
<td align="center">
    <a href="https://github.com/{github_username}">
    <img src="https://avatars.githubusercontent.com/{github_username}?s=150&v=1" width="100px;" alt="{github_username}"/>
    </a>
    <br/>
    <a href="https://github.com/{github_username}">{name}</a>
</td>
'''

output = ''

def first_capital(title):
    return f"{title[0].upper()}{title[1:]}"

with open(filename) as fp:
    data = json.load(fp)

    for key in data.keys():
        title = first_capital(key)

        output += f'{title_template.format(title)}\n'

        row_data = ''

        for value in data[key]:
            row_data += f"{user_template.format(github_username=value['github_username'], name=value['name'])}\n"

        output += f'{base_template.format(row_data)}\n'
    
with open(output_filename, 'w') as fp:
    output = "<!--- Use [parse_contributors.py] to generate this file -->\n{output}"
    fp.write(output)


    
