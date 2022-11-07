## Copyrights : Sushan Shakya

## Use this script to generate snippet for contributors

import json

filename = "contributors.json"
output_filename = "contributors.md"


title_template = '> {}'

base_template = '''
<table>
{}
</table>
'''

table_row = '''
<tr>
{}
</tr>
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

def get_rowed_data(data):
    result = [[]]
    item_in_a_row = 5
    cur = 0
    filled = False
    for i in range(len(data)):
        result[cur].append(data[i])
        filled = False
        if(((i + 1) % item_in_a_row) == 0):
            filled = True
        if(filled) :
            result.append([])
            cur= cur + 1
    
    return result


# print(get_rowed_data([1,2,3,4,5,6,7,8]))
# print(get_rowed_data([1,2,3,4,5,6,7,8,9,10,11,12]))

with open(filename) as fp:
    data = json.load(fp)

    for key in data.keys():
        title = first_capital(key)

        output += f'{title_template.format(title)}\n'

        row_data = ''

        tech_stacks = data[key]

        rowed_data = get_rowed_data(tech_stacks)

        for tech_stacks in rowed_data:
            tmp = ''
            tmp = f"<tr>{tmp}"
            for value in tech_stacks:
                tmp += f"{user_template.format(github_username=value['github_username'], name=value['name'])}\n"
            tmp = f"{tmp}</tr>"
            row_data = f"{row_data}{tmp}"

        output += f'{base_template.format(row_data)}\n'
    
with open(output_filename, 'w') as fp:
    output = f"<!--- Use [parse_contributors.py] to generate this file -->\n\n## Contributors\n<br><br>\n{output}"
    fp.write(output)


    
