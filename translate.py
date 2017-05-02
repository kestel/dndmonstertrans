#!/usr/bin/env python3.6
#-*- coding:utf-8 -*-

import re
# подцепляем словарь из внешнего файла
import translate_dict as d

def replace_lang(text, dic):
    """Заменялка для языков"""
    text = text.replace("Languages:", "Languages")
    if "---" in text:
        return text
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
    """
    Заменяем всё подряд, что не попало под другие фильтры но в нижнем регистре
    Используется в замене заклинаний
    """
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
    match = re.search(r"Challenge[\s:]+(?P<cr>[\d\/]+)\s\((?P<xp>[\d\s,]+)\sXP\)", line)
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
    newline = "{}:".format(spell_list[0])
    for spell in spell_list[1:]:
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

        elif re.search("Cantrip|[\d\w\s]{4}level|\d\/day\seach|At\swill", line, re.IGNORECASE):
            line = translate_spell(line)

        elif "pack tactics" in line_lower:
            line = re.sub(r"Pack Tactics. ([\s\w]+) has advantage on an attack roll against a creature if at least one of the (\w+).+",
                          r"Тактика стаи. \1 совершает с преимуществом броски атаки по существу, если в пределах 5 футов от этого существа находится как минимум один дееспособный союзник \2",
                          line)

        elif "keen smell" in line_lower:
            line = re.sub(r"Keen Smell. ([\s\w]+) has advantage on Wisdom \(Perception\) checks that rely on smell.+",
                          r"Тонкий нюх. \1 совершает с преимуществом проверки Мудрости (Внимательность), полагающиеся на обоняние",
                          line)

        elif "keen sight and smell" in line_lower:
            line = re.sub(r"Keen Sight and Smell. ([\s\w]+) has advantage on Wisdom \(Perception\) checks that rely on sight or smell.+",
                          r"Острый слух и тонкий нюх. \1 совершает с преимуществом проверки Мудрости (Внимательность), полагающиеся на слух и обоняние",
                          line)

        elif "innate spellcasting" in line_lower:
            line = re.sub(r"Innate Spellcasting. ([\s\w\']+) innate spellcasting ability is ([\w]+). It can innately cast the following spells, requiring no material components:",
                          r"Врождённое колдовство. Базовой характеристикой \1 является \2. Он может накладывать следующие заклинания, не нуждаясь ни в каких компонентах:",
                          line)

        elif "spellcasting" in line_lower:
            line = re.sub(r"Spellcasting. ([\s\w]+) is a.? ([\d]+)[\w]+-level spellcaster.",
                          r"Колдовство. \1 является заклинателем \2 уровня.",
                          line)
            line = re.sub(r"Its spellcasting ability is (\w+) \(spell save(?:\sDC|)\s(\d+), ([\d+]+) to hit with spell attacks\).",
                          r"Его способность к заклинаниям основана на \1 (Сл спасброска от заклинаний \2, \3 к атакам заклинаниями).",
                          line)
            line = re.sub(r"([\s\w]+) has the following (?:(\w+)\s|)spells prepared",
                          r"\1 обладает следующими заготовленными заклинаниями \2",
                          line)
        elif "change shape" in line_lower:
            line = re.sub(r"Change Shape. ([\s\w]+) magically polymorphs into a ([\s\w]+) it has seen, or back into its true form.",
                          r"Смена формы. \1 магическим образом превращается в \2, которого видел, или принимает свой истинный облик.",
                          line)
        elif ("target must make" and "saving throw") in line_lower:
            line = re.sub(r"The target must make a DC (\d+) (\w+) saving throw",
                          r"Цель должна совершить спасбросок \2 со Сл \1",
                          line)

        # else:
        #    print(line_lower)

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
