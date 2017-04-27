#!/usr/bin/env python3.6
#-*- coding:utf-8 -*-

import re
# подцепляем словарь из внешнего файла
import translate_dict as d

def replace_lang(text, dic):
    """Заменялка для языков"""
    langs = re.findall('(?:^Languages|(?<= ))(\w+)[, ]*', text)
    langru = "Языки "
    for lang in langs:
        try:
            langru = langru + dic[lang] + ", "
        except:
            return text
            
    return langru[:-2]


def replace_other(line, dic):
    """Заменяем всё подряд, что не попало под другие фильтры"""
    for i, j in dic.items():
        line = line.replace(i, j)

    return line


def replace_other_lower(line, dic):
    """Заменяем всё подряд, что не попало под другие фильтры"""
    for i, j in dic.items():
        line = line.replace(i.lower(), j.lower())

    return line


def fix_symbols(line):
    """Эта хрень нужна для исправления отображения разных символов"""
    line = line.replace(b'\xc3\xa2\xc2\x88\xc2\x92'.decode('utf-8'), "-").\
        replace(b'\xc3\xa2\xc2\x80\xc2\x99'.decode('utf-8'), "'").\
        replace('Â¬', '').\
        replace('¬', '').\
        replace("’", "'")
    
    return line


def replace_cr(line):
    match = re.search(r"Challenge\s(?P<cr>[\d\/]+)\s\((?P<xp>[\d\s,]+)\sXP\)", line)
    if match:
        cr = str(match.group('cr'))
        xp = int(match.group('xp').replace(" ", "").replace(",", ""))
    line = "Опасность {cr} ({xp} опыта)".format(cr=cr, xp=xp)
    
    return line


def replace_multiattack(line):
    line = line.replace("Multiattack", "Мультиатака").replace("melee attacks", "рукопашные атаки").\
        replace("ranged attacks", "дальнобойные атаки").replace("attacks", "атаки").replace("makes", "делает")

    return line


def translate_spell(line):
    line = line.replace(";", ",").replace(":", ",")
    spell_list = line.split(",")
    newline = ""
    for spell in spell_list:
        spell_ru = replace_other_lower(spell.strip(), d.spell_dict)
        newline = "{0} {1} [{2}], ".format(newline.strip(), spell_ru.strip(), spell.strip())

    return newline[:-2]


def replacer(text, dic):
    """Основная функция, которая делает всю работу. В том числе запускает другие функции"""
    translated_text = ""

    for line in text.splitlines():
        line = fix_symbols(line)
        line_lower = line.lower()
        
        if "languages" in line_lower:
            line = replace_lang(line, d.lang_dict)
            
        elif "multiattack" in line_lower:
            line = replace_multiattack(line)
            
        elif "challenge" in line_lower:
            line = replace_cr(line)

        elif ("at will" or "cantrip" or "1st level") in line_lower:
            line = translate_spell(line)

        elif ("2nd level" or "3rd level" or "4th level" or "5th level") in line_lower:
            line = translate_spell(line)

        elif ("6th level" or "7th level" or "8th level" or "9th level") in line_lower:
            line = translate_spell(line)

        else:
            print(line_lower)

        """Замена всего оставшегося"""
        line = replace_other(line, dic)

        """Замена кубов по всему тексту"""
        line = re.sub(r"(\d+)d(\d+)", r"\1к\2", line)
        
        """Собираем текст заново построчно (с виндовым переносом строки)"""
        translated_text = translated_text + "\r\n" + line
               
    return translated_text


def main():
    import sys
    input_text = None
    filename = None

    try:
        filename = sys.argv[1]
    except IndexError:
        print("Should specify input filename")
        sys.exit(1)

    with open(filename, 'r') as f:
        input_text = f.read()
    
    translated_text = replacer(input_text, d.all_dict)
    print(translated_text)


if __name__ == "__main__":
    main()
