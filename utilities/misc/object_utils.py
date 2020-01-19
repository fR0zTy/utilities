# -*- coding : utf-8 -*-


def iter_attributes(obj, protected=False):
    class_name = obj.__class__.__name__
    for attr in vars(obj):
        invalid = (not protected and attr.startswith("_")) or attr.startswith(f'_{class_name}')
        if invalid:
            continue
        yield attr
