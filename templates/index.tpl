% include("templates/header.tpl", title="Переводчик копи-паста!")

<div id="form">
<form action="/translate" method="post">
<textarea cols="80" rows="24" name="text" style="height:450px; width:100%; max-width:600px"></textarea>
<br />
<input type="submit" style="height:50px; width:59%" value="Перевести"> <input type="reset" style="height:50px; width:39%" value="Очистить">
</form></div>
<br />

<details>
<summary><span>Пример перевода монстра (Rakshasa)</span></summary>
<span><form action="/translate" method="post">
<textarea hidden cols="80" rows="24" name="text" style="height:450px; width:500px">Rakshasa

Medium fiend, lawful evil

Armor Class 16 (natural armor)
Hit Points 110 (13d8 + 52)
Speed 40 ft.
STR 	DEX 	CON 	INT 	WIS 	CHA
14 (+2) 	17 (+3) 	18 (+4) 	13 (+1) 	16 (+3) 	20 (+5)

Skills Deception +10, Insight +8
Damage Vulnerabilities piercing from magic weapons wielded by good creatures
Damage Immunities bludgeoning, piercing, and slashing from nonmagical attacks
Senses darkvision 60 ft., passive Perception 13
Languages Common, Infernal
Challenge 13 (10,000 XP)

Special Traits
Limited Magic Immunity: The rakshasa can’t be affected or detected by spells of 6th level or lower unless it wishes to be. It has advantage on saving throws against all other spells and magical effects.
Innate Spellcasting: The rakshasa’s innate spellcasting ability is Charisma (spell save DC 18, +10 to hit with spell attacks). The rakshasa can innately cast the following spells, requiring no material components:
At will: detect thoughts, disguise self, mage hand, minor illusion
3/day each: charm person, detect magic, invisibility, major image, suggestion
1/day each: dominate person, fly, plane shift, true seeing

Actions
Multiattack: The rakshasa makes two claw attacks.
Claw: Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) slashing damage, and the target is cursed if it is a creature. The magical curse takes effect whenever the target takes a short or long rest, filling the target’s thoughts with horrible images and dreams. The cursed target gains no benefit from finishing a short or long rest. The curse lasts until it is lifted by a remove curse spell or similar magic.

</textarea>
<br />
<input type="submit" style="height:50px; width:99%" value="Посмотреть пример перевода">
</form></span>
</details><br />

Предложить вариант перевода можно через <a href="https://goo.gl/forms/MaaIYAuvFfIT4eQL2">форму</a>.<br /><br />

Исходные коды доступны на <a href="https://github.com/kestel/dndmonstertrans">https://github.com/kestel/dndmonstertrans</a><br /><br />

Последняя дата обновления: {{latest_commit_date}}
