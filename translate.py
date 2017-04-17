#!/usr/bin/env python3.5

import re
# подцепляем словарь из внешнего файла
import translate_dict as dictionary


input_text = None
filename = None


def replace_lang(text, dic):
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


def replacer(text, dic):
    translated_text = ""
    for line in text.splitlines():
        line = line.replace(b'\xc3\xa2\xc2\x88\xc2\x92'.decode('utf-8'), '-')
        line = line.replace(b'\xc3\xa2\xc2\x80\xc2\x99'.decode('utf-8'), "'")
        if "languages" in line.lower():
            line = replace_lang(line, dictionary.lang_dict)
            
        if "multiattack" in line.lower():
            line = re.sub(r"Multiattack. ([\s\w]+) makes (\w+) melee.+", r"Мультиатака. \1 делает \2 рукопашные атаки.", line)
            line = re.sub(r"Multiattack. ([\s\w]+) makes (\w+) ranged.+", r"Мультиатака. \1 делает \2 дальнобойные атаки.", line)
            
        # замена кубов по всему тексту
        line = re.sub(r"(\d+)d(\d+)", r"\1к\2", line)

        # замена всего подряд
        line = replace_other(line, dic)
        
        # и собираем текст заново построчно
        translated_text = translated_text + "\r\n" + line
               
    return translated_text


def main():
    import sys
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Should specify input filename")
        sys.exit(1)

    with open(filename, 'r') as f:
        input_text = f.read()
    
    translated_text = replacer(input_text, dictionary.all_dict)
    print(translated_text)


if __name__ == "__main__":
    main()
