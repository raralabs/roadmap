# How to generate contributors

## Hey There I am presuming that you're a dev. trying to add yourself to contributors.

    You'll need python installed on your machine to generate the data though ╰(*°▽°*)╯

### Step 1 : 
Modify the `contributors.json` file and add your name and github username in the following format :

    "<some_list_name>" : [
        ...,
        {
            "name": "Sushan Shakya",
            "github_username": "SushanShakya"
        },
        ...
    ]

### Step 2 :
Inside the `roadmap` project run the following script :

For Unix based Environment

    > python ./parse_contributors.py


For Windows based Environment

    > python .\parse_contributors.py


### `Done !!! You've generated the contributors.`