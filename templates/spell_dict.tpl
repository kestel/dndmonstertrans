% include("templates/header.tpl", title="Словарь заклинаний")

<a href="#phb">PHB</a>&nbsp;&nbsp;
<a href="#EE">Elemental Evil</a>&nbsp;&nbsp;
<a href="#scag">Swords Coast Adventure Guide</a>&nbsp;&nbsp;
<a href="#tfyp">Tales from Yawning Portal</a>&nbsp;&nbsp;


<h3 id="phb">PHB</h3>
<table border=0 width=500>
%for elem in phb_spell:
<tr><td width="250">{{elem}}</td><td>{{phb_spell[elem]}}</td></tr>
%end
</table>

<h3 id="ee">Elemental Evil</h3>
<table border=0 width=500>
%for elem in ee_spell:
<tr><td width="250">{{elem}}</td><td>{{ee_spell[elem]}}</td></tr>
%end
</table>

<h3 id="scag">Swords Coast Adventure Guide</h3>
<table border=0 width=500>
%for elem in scag_spell:
<tr><td width="250">{{elem}}</td><td>{{scag_spell[elem]}}</td></tr>
%end
</table>

<h3 id="tfyp">Tales from Yawning Portal</h3>
<table border=0 width=500>
%for elem in tfyp_spell:
<tr><td width="250">{{elem}}</td><td>{{tfyp_spell[elem]}}</td></tr>
%end
</table>

<br />Вернуться на <a href='/'>главную</a>.<br />
