from random import randint
from os import path
import sys
sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '.')))

from __hex_constants__ import __hex_letters, __alphabet
from intohex import _intohex as intohex
from hextoint import _hextoint as hextoint


def packtwo(target, prefix=False):
    if type(target) != str:
        raise ValueError("Argument must be string")
    if type(target) not in (bool, str):
        raise ValueError("prefix must be string or boolean")
    if prefix != False:
        if prefix == True:
            target = target[2:]
        if type(prefix) is str:
            target = target[len(prefix):]
    hex_pairs = []
    _x = 0
    _y = 2
    while _y <= len(target):
        hex_pairs.append(target[_x:_y])
        _x = _y
        _y += 2
    if (len(target) % 2 != 0):
        if any(item==target[-1] for item in hex_pairs) == False:
            hex_pairs.append(target[-1])
    return(hex_pairs)


def _abctohex(target, conversion="ord", verbose=False, prefix=False, individual_prefix=False):
    if type(target) != str:
        raise ValueError("Target must be string")
    if type(verbose) not in (int, bool):
        raise ValueError("Verbose must be bool or int")
    if type(prefix) not in (bool, str):
        raise ValueError("prefix must be bool or string")
    if type(individual_prefix) not in (bool, str):
        raise ValueError("individual_prefix must be bool or string")


    result_list = []
    result_str = None

    if conversion is "alphabet":
        for item in target:
                if item in [str(x) for x in list(range(0, 10))]:
                    result_list.append(item)
                else:
                    result_list.append(intohex(__alphabet.index(item.lower())))
                # print(item, __alphabet.index(item), intohex(__alphabet.index(item), True))
        # print("".join(item for item in result_list))
        result_str = "".join(item for item in result_list)

    elif conversion is "ord":
        for item in target:
                result_list.append(intohex(ord(item)))
                # print(item, ord(item), intohex(ord(item), True))
        # print("".join(item for item in result_list))
        result_str = "".join(item for item in result_list)
    else:
        raise ValueError("conversion has to be \'alphabet\' or \'ord\'")
    if prefix is True:
        if individual_prefix:
            if individual_prefix is True:
                prefixer = "0x"
            elif type(individual_prefix) is str:
                prefixer = individual_prefix
            pairs = list(packtwo(result_str))
            for item in pairs:
                pairs[pairs.index(item)] = (prefixer + item) if prefixer != '\\x' else (prefixer + item)[1:]
            return("".join(pairs))
        else:
            if type(prefix) is str:
                result_str = prefix + result_str
            else:
                result_str = "0x" + result_str
    return(result_str)


def _hextoabc(target):
    char_hex = []
    for item in packtwo(target):
        char_hex.append(chr(hextoint(item)))
    return("".join(char_hex))
