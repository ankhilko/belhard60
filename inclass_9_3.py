import yaml
from yaml.loader import SafeLoader

data = {
    'name': 'alex',
    'email': 'a@nib.com',
    'age': 45,
    'languages': ['EN', 'DE', 'RU']
}


with open('out_yaml.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(data, file)


with open('out_yaml_safe.yaml', 'w', encoding='utf-8') as file:
    yaml.safe_dump(data, file)


with open('out_yaml.yaml', 'r', encoding='utf-8') as file:
    data1 = yaml.safe_load(file)

    print(data1)

