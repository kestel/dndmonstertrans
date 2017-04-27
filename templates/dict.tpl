% include("templates/header.tpl", title="Словарь перевода")

Вернуться на <a href='/'>главную</a>.<br /><br />

<div id="menu"><a href="#common">Общий термины</a>&nbsp;&nbsp;<a href="#damage">Урон</a>&nbsp;&nbsp;
<a href="#alignment">Мировоззрения</a>&nbsp;&nbsp;<a href="#creature">Описания существ</a>&nbsp;&nbsp;
<a href="#lang">Языки</a>&nbsp;&nbsp;<a href="#condition">Состояния</a>&nbsp;&nbsp;
<a href="#skill">Скиллы (навыки)</a>&nbsp;&nbsp;<a href="#armor">Доспехи</a>&nbsp;&nbsp;
<a href="#weapon">Оружие</a>&nbsp;&nbsp;<a href="#race">Расы</a>&nbsp;&nbsp;<a href="#abilities">Способности</a>&nbsp;&nbsp;</div>


<h3 id="common">Общие термины</h3>
<table border=0 width=500>
%for elem in common_dict:
<tr><td width="250">{{elem}}</td><td>{{common_dict[elem]}}</td></tr>
%end
</table>

<h3 id="damage">Урон</h3>
<table border=0 width=500>
%for elem in damage_dict:
<tr><td width="250">{{elem}}</td><td>{{damage_dict[elem]}}</td></tr>
%end
</table>

<h3 id="alignment">Мировоззрения</h3>
<table border=0 width=500>
%for elem in alignment_dict:
<tr><td width="250">{{elem}}</td><td>{{alignment_dict[elem]}}</td></tr>
%end
</table>

<h3 id="creature">Описания существ</h3>
<table border=0 width=500>
%for elem in creature_dict:
<tr><td width="250">{{elem}}</td><td>{{creature_dict[elem]}}</td></tr>
%end
</table>

<h3 id="lang">Языки</h3>
<table border=0 width=500>
%for elem in lang_dict:
<tr><td width="250">{{elem}}</td><td>{{lang_dict[elem]}}</td></tr>
%end
</table>

<h3 id="condition">Состояния</h3>
<table border=0 width=500>
%for elem in condition_dict:
<tr><td width="250">{{elem}}</td><td>{{condition_dict[elem]}}</td></tr>
%end
</table>

<h3 id="skill">Скиллы (Навыки)</h3>
<table border=0 width=500>
%for elem in skill_dict:
<tr><td width="250">{{elem}}</td><td>{{skill_dict[elem]}}</td></tr>
%end
</table>

<h3 id="armor">Доспехи</h3>
<table border=0 width=500>
%for elem in armor_dict:
<tr><td width="250">{{elem}}</td><td>{{armor_dict[elem]}}</td></tr>
%end
</table>

<h3 id="weapon">Оружие</h3>
<table border=0 width=500>
%for elem in weapon_dict:
<tr><td width="250">{{elem}}</td><td>{{weapon_dict[elem]}}</td></tr>
%end
</table>

<h3 id="race">Расы</h3>
<table border=0 width=500>
%for elem in race_dict:
<tr><td width="250">{{elem}}</td><td>{{race_dict[elem]}}</td></tr>
%end
</table>

<h3 id="abilities">Способности</h3>
<table border=0 width=500>
%for elem in abilities_dict:
<tr><td width="250">{{elem}}</td><td>{{abilities_dict[elem]}}</td></tr>
%end
</table>

<br />Вернуться на <a href='/'>главную</a>.<br />
