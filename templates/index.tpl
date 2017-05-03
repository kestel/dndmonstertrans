% include("templates/header.tpl", title="Переводчик копи-паста!")

<p>Посмотреть <a href="/dict">Общий словарь</a> замены. Или <a href="/spell_dict">Словарь заклинаний</a></p>

<form action="/translate" method="post">
<textarea cols="80" rows="24" name="text" style="height:450px; width:650px"></textarea>
<br />
<input type="submit" style="height:50px; width:500px" value="Перевести текст"> <input type="reset" style="height:50px; width:150px" value="Очистить поле">
</form><br />

Предложить вариант перевода можно через <a href="https://goo.gl/forms/MaaIYAuvFfIT4eQL2">форму</a>.<br /><br />

Исходные коды доступны на <a href="https://github.com/kestel/dndmonstertrans">https://github.com/kestel/dndmonstertrans</a><br /><br />

Последняя дата обновления: {{latest_commit_date}}