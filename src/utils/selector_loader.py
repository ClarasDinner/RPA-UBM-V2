import yaml

def load_selectors(path='config/selectors.yaml'):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)