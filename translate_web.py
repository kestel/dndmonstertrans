#!/usr/bin/env python3.6
#-*- coding:utf-8 -*-

import sys
from os import environ
# подцепляем словарь из внешнего файла
import translate_dict as d
import spell_dict as s
from translate import replacer
import bottle

bottle.debug(True)


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
                           weapon_dict=d.weapon_dict,
                           race_dict=d.race_dict,
                           abilities_dict=d.abilities_dict,
                           name_dict=d.name_dict)
    return html


@bottle.route('/spell_dict')
def print_spell_dict():
    html = bottle.template("templates/spell_dict.tpl",
                           phb_spell=s.phb_spell,
                           ee_spell=s.ee_spell,
                           scag_spell=s.scag_spell,
                           tfyp_spell=s.tfyp_spell)
    return html


@bottle.post('/translate')
def print_translate():
    input_text = None
    input_text = bottle.request.forms.text
    if input_text:
        text = replacer(input_text, d.all_dict)
    else:
        text = "Кажется, вы не ввели текст."
    html = bottle.template("templates/translate.tpl", text=text)
    return html


@bottle.route('/')
def print_index():
    latest_commit_date = None
    try:
        latest_commit_date = environ["UPDATED_DATE"]
    except:
        latest_commit_date = "Не доступно"
    html = bottle.template("templates/index.tpl", latest_commit_date=latest_commit_date)
    return html


bottle.run(host='0.0.0.0', port=sys.argv[1])
