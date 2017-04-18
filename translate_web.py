#!/usr/bin/env python3.6

import sys
# подцепляем словарь из внешнего файла
import translate_dict as d
from translate import replacer
import bottle

bottle.debug(True)

input_text = None

@bottle.route('/dict')
def print_dict():
    html = bottle.template("templates/dict.tpl",
        common_dict=d.common_dict,
        damage_dict=d.damage_dict,
        alignment_dict=d.alignment_dict,
        creature_dict=d.creature_dict,
        lang_dict=d.lang_dict,
        condition_dict=d.condition_dict,
        skill_dict=d.skill_dict,
        armor_dict=d.armor_dict,
        weapon_dict=d.weapon_dict )
    return html
    
    
@bottle.post('/translate')
def print_translate():
    input_text = bottle.request.forms.get('text')
    if input_text:
        return "Вернуться на <a href='/'>главную</a>.<br />\n<pre>"+replacer(input_text, d.all_dict)+"</pre>"
    else:
        return "Вернуться на <a href='/'>главную</a>.<br />\nКажется, вы не ввели текст."


@bottle.route('/')
def print_index():
    html = bottle.template("templates/index.tpl")
    return html

bottle.run(host='0.0.0.0', port=sys.argv[1])

