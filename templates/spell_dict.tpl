% include("templates/header.tpl", title="Словарь заклинаний")

Вернуться на <a href='/'>главную</a>.<br /><br />

<a href="#spell">Заклинания</a>


<h3 id="spell">Заклинания</h3>
<table border=0 width=500>
%for elem in spell_dict:
<tr><td width="250">{{elem}}</td><td>{{spell_dict[elem]}}</td></tr>
%end
</table>

<br />Вернуться на <a href='/'>главную</a>.<br />
