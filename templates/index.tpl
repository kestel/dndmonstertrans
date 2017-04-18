% include("templates/header.tpl", title="Переводчик копи-паста!")

<p>Посмотреть <a href="/dict">словарь</a> замены</p>
<form action="/translate" method="post">
<textarea cols="80" rows="24" name="text"></textarea>
<br />
<input type="submit" value="Перевести текст"> <input type="reset" value="Очистить поле">
</form><br />

Исходные коды доступны на <a href="https://github.com/kestel/dndmonstertrans">https://github.com/kestel/dndmonstertrans</a>
