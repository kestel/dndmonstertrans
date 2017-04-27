% include("templates/header.tpl", title="Словарь заклинаний")

Вернуться на <a href='/'>главную</a>.<br /><br />

<a href="#phb">PHB</a>&nbsp;&nbsp;<a href="#tfyp">Tales from Yawning Portal</a>&nbsp;&nbsp;


<h3 id="phb">PHB</h3>
<table border=0 width=500>
%for elem in phb_spell:
<tr><td width="250">{{elem}}</td><td>{{phb_spell[elem]}}</td></tr>
%end
</table>

<h3 id="tfyp">Tales from Yawning Portal</h3>
<table border=0 width=500>
%for elem in tfyp_spell:
<tr><td width="250">{{elem}}</td><td>{{tfyp_spell[elem]}}</td></tr>
%end
</table>

<br />Вернуться на <a href='/'>главную</a>.<br />
