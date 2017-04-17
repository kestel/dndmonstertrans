#!/usr/bin/env python3.5

import sys
# подцепляем словарь из внешнего файла
import translate_dict as dictionary
from translate import replacer
import bottle

bottle.debug(True)

input_text = None


@bottle.route('/dict')
def print_dict():
    dict_text = "<h3>Список языков:</h3>\n<br /><pre>"
    for elem in dictionary.lang_dict:
        dict_text = dict_text + elem + ": " + dictionary.lang_dict[elem] + "</br />\n"
    dict_text = dict_text + "</pre>\n<h3>Всё вперемешку:</h3><br /><pre>"
    for elem in dictionary.all_dict:
        if elem:
            dict_text = dict_text + elem + ": " + dictionary.all_dict[elem] + "</br />\n"
    dict_text = dict_text + "</pre>"
    return dict_text
    
    
@bottle.post('/translate')
def print_translate():
    input_text = bottle.request.forms.get('text')
    if input_text:
        return "Вернуться на <a href='/'>главную</a>.<br />\n<pre>"+replacer(input_text, dictionary.all_dict)+"</pre>"
    else:
        return "Вернуться на <a href='/'>главную</a>.<br />\nКажется, вы не ввели текст."


@bottle.route('/')
def print_index():
    return """
    <p>Посмотреть <a href="/dict">словарь</a> замены</p>
    <form action="/translate" method="post">
    <textarea cols="80" rows="24" name="text"></textarea>
    <br />
    <input type="submit" value="Перевести текст"> <input type="reset" value="Очистить поле">
    </form>
    """

bottle.run(host='0.0.0.0', port=sys.argv[1])

