from importlib.metadata import EntryPoint, entry_points as iter_entry_points
from collections.abc import Set, Mapping
import typing as t

def entry_point_getter(attrs):
    """
    attrs: t.Tuple[str|None,str|None,str|None]

    return: t.Set[EntryPoint]
    """
    name, value, group = attrs

    if not group:
        raise RuntimeError('Entry point group required')

    try:
        entry_point_grp = iter_entry_points()[group]
    except KeyError:
        return set()
    
    ret = set()
    
    for ep in entry_point_grp:
        if not name:
            name_match = True
        else:
            name_match = name == ep.name

        if not value:
            value_match = True
        else:
            value_match = value == ep.value

        if name_match and value_match:
            ret.add(ep)
    
    return ret

def get_partially_ordered_list(total_set,
                               initial_set = set(),
                               ordered_list = []):
    """
    total_set: Set[EntryPoint]
    initial_set: Set[EntryPoint] = set()
    ordered_list: t.List[EntryPoint] = []

    return: t.List[EntryPoint]
    """
                             
    return list(initial_set) + ordered_list + list(total_set - initial_set - set(ordered_list))
    
