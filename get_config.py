from yaml import load as yaml_load, SafeLoader
from munch import DefaultMunch


def get_conf() -> DefaultMunch:
    with open(f'config_ssh.yaml', 'r') as settings:
        config = DefaultMunch.fromDict(yaml_load(settings, SafeLoader))
    return config
