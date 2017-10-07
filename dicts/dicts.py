#-*- coding:utf-8 -*-

from dicts.spells import spell_dict
from dicts.items import weapon_dict, armor_dict, equipment_packs_dict, tools_dict, mounts_vehicles_dict, adventuring_gear_dict
from dicts.creatures import  creature_dict
from dicts.abilities import abilities_dict
from dicts.names import name_dict


common_dict = {
    "Armor Class ": "Класс Доспеха ",
    "Hit Points ": "Хиты ",
    "Speed ": "Скорость ",
    "Armor Class: ": "Класс Доспеха ",
    "Hit Points: ": "Хиты ",
    "Speed: ": "Скорость ",
    "ft.": "фт.",
    "Saving Throws ": "Спасброски ",
    "Saving Throws: ": "Спасброски ",
    " fly ": " полёт ",
    " swim ": " плавание ",
    " burrow ": " рытьё ",
    " climb ": " взбирание ",
    " hover ": " парение ",
    "Special Senses ": "Чувства ",
    "Senses ": "Чувства ",
    "Senses: ": "Чувства ",
    " darkvision ": " тёмное зрение ",
    " truesight ": " истинное зрение ",
    "passive Perception": "пассивное Восприятие",
    "passive ": "пассивное ",
    "Special Traits": "Особые черты",
    "Condition Immunities": "Иммунитет к состояниям",
    "Condition immunities": "Иммунитет к состояниям",
    "poisoned": "отравленный",
    "tremorsense": "чувство дрожи",
    "blindsight": "слепое зрение",
    "Challenge ": "Опасность ",
    " XP)": " опыта)",
    "Actions": "Действия",
    "ACTIONS": "Действия",
    "Multiattack.": "Мультиатака.",
    "one target": "одна цель",
    "Hit: ": "Попадание: ",
    "Melee or Ranged Weapon Attack:": "Рукопашная или дальнобойная атака оружием:",
    "Melee Weapon Attack:": "Рукопашная атака оружием:",
    "Melee Weapon attack:": "Рукопашная атака оружием:",
    "Ranged Weapon Attack: ": "Дальнобойная атака оружием: ",
    "Ranged Weapon attack: ": "Дальнобойная атака оружием: ",
    "(Recharge": "(Перезарядка",
    "Damage Vulnerabilities ": "Уязвимость к урону ",
    "Melee Spell Attack:": "Рукопашная атака заклинанием:",
    "Ranged Spell Attack:": "Дальнобойная атака заклинанием:",
    " to hit, reach ": " к попаданию, досягаемость ",
    " to hit, range": " к попаданию, дистанция",
    "Cantrips": "Заговоры",
    "Cantrip": "Заговор",
    "at will": "неограниченно",
    "At will": "Неограниченно",
    "telepathy": "телепатия",
    "understands": "понимает",
    "but can't speak": "но не может говорить",
    "from nonmagical attacks": "от немагических атак",
# параметры
    "STR": "СИЛ",
    "DEX": "ЛОВ",
    "CON": "ТЕЛ",
    "INT": "ИНТ",
    "WIS": "МДР",
    "CHA": "ХАР",
    "Str ": "Сил ",
    "Dex ": "Лов ",
    "Con ": "Тел ",
    "Int ": "Инт ",
    "Wis ": "Мдр ",
    "Cha ": "Хар ",
    "Strength": "Сила",
    "Dexterity": "Ловкость",
    "Constitution": "Телосложение",
    "Intelligence": "Интеллект",
    "Wisdom": "Мудрость",
    "Charisma": "Харизма",
}

damage_dict = {
# типы урона
    " lightning damage": " урон электричеством",
    " damage ": " урон ",
    " damage.": " урон.",
    " damage,": " урон,",
    " plus ": " плюс ",
    " piercing": " колющий",
    " bludgeoning": " дробящий",
    " slashing": " рубящий",
    " fire": " огненный",
    " cold": " холод",
    " poison": " яд",
    " psychic": " психический",
    " acid": " кислотный",
    " lightning": " электрический",
    " necrotic": " некротический",
    " radiant": " излучение",
    " force": "силовым полем",
}

alignment_dict = {
# мировоззрения
    "chaotic evil": "хаотично-злой",
    "lawful evil": "законно-злой",
    "neutral evil": "нейтрально-злой",
    "chaotic good": "хаотично-добрый",
    "lawful good": "законно-добрый",
    "neutral good": "нейтрально-добрый",
    "chaotic neutral": "хаотично-нейтральный",
    "lawful neutral": "законно-нейтральный",
    "neutral": "нейтральный",
    "unaligned": "без мировоззрения",
    "any non-good alignment": "любое не хорошее мировоззрение",
    "any good alignment": "любое хорошее мировоззрение",
    "any alignment": "любое мировоззрение",
}

lang_dict = {
    "Languages ": "Языки ",
    "Languages: ": "Языки ",
    "Abyssal": "Бездны",
    "Bothii": "Ботхи",
    "Common": "Общий",
    "Celestial": "Небесный",
    "Deep Speech": "Глубинная речь",
    "Draconic": "Драконий",
    "Dwarvish": "Дварфийский",
    "Dwarwish": "Дварфийский",
    "Elvish": "Эльфийский",
    "Giant": "Язык гигантов",
    "Goblin": "Гоблинский",
    "Hafling": "Халфлингов",
    "Ignan": "Игнан",
    "Infernal": "Инфернальный",
    "Orc": "Орочий",
    "Sylvan": "Сильван",
    "Telepathy": "Телепатия",
    "Undercommon": "Подземный",
    "Yikaria ": "Икария",
    "Aquan": "Акван",
    "Auran": "Ауран",
    "Terran": "Терран",
    "Primordial": "Первичный",
}

condition_dict = {
    "": "",
    "Blinded": "Ослеплённый",
    "blinded": "Ослеплённый",
    "charmed": "Очарованный",
    "Charmed": "Очарованный",
    "Deafened": "Оглохший",
    "deafened": "Оглохший",
    "Exhaustion": "Истощение",
    "exhaustion": "Истощение",
    "Frightened": "Испуганный",
    "frightened": "Испуганный",
    "Grappled": "Схваченный",
    "grappled": "Схваченный",
    "Incapacitated": "Недееспособный",
    "incapacitated": "Недееспособный",
    "Invisible": "Невидимый",
    "invisible": "Невидимый",
    "Paralyzed": "Парализованный",
    "paralyzed": "Парализованный",
    "Petrified": "Окаменевший",
    "petrified": "Окаменевший",
    "Poisoned": "Отравленный",
    "poisoned": "Отравленный",
    "Prone": "Лежащий ничком",
    "prone": "Лежащий ничком",
    "Restrained": "Удерживаемый",
    "restrained": "Удерживаемый",
    "Stunned": "Ошеломлённый",
    "stunned": "Ошеломлённый",
    "Unconscious": "Бессознательный",
    "unconscious": "Бессознательный",
}

skill_dict = {
    "Skills ": "Навыки ",
    "Skills: ": "Навыки ",
    "Acrobatics ": "Акробатика ",
    "Animal Handling ": "Уход за животными ",
    "Arcana ": "Магия ",
    "Athletics ": "Атлетика ",
    "Deception ": "Обман ",
    "History ": "История ",
    "Insight ": "Проницательность ",
    "Intimidation ": "Запугивание ",
    "Investigation ": "Расследование ",
    "Medicine ": "Медицина",
    "Nature": "Природа",
    "Perception": "Восприятие",
    "Performance ": "Выступление ",
    "Persuasion ": "Убеждение ",
    "Religion ": "Религия ",
    "Sleight of Hand ": "Ловкость рук ",
    "Stealth ": "Скрытность ",
    "Survival ": "Выживание ",
}

race_dict = {
    "Aasimar": "Аасимар",
    "Half-Elf": "Полуэльф",
    " Elf ": " Эльф ",
}


item_dict = {**weapon_dict, **armor_dict}

# В all_dict не включается lang_dict т.к. тогда поедут названия монстров типа Goblin, Orc
all_dict = {**abilities_dict, **spell_dict, **common_dict, **skill_dict, **condition_dict, **item_dict,
    **alignment_dict, **creature_dict, **damage_dict, **race_dict, **name_dict}
