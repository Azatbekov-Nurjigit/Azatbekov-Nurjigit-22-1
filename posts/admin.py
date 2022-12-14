from django.contrib import admin
from posts.models import Post ,Hashtag,Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Hashtag)
admin.site.register(Comment)



# 1) <a></a> - ссылка
# 2) <h1></h1> - заголовок
# 3) <strong></strong> - жирный текст
# 4) <em></em> - курсивный текст
# 5) <small></small> - маленький текст
# 6) <br> - новая строка
# 7) <p></p> - создать параграф
# 8) <ol></ol> - список (цифрами)
#    <ul></ul> - список (точками)
#    <li></li> - использовать между UL и OL
# 9) <img src="копировать URL"> - добавить фото
#    <img width="***px"> - размер картинки (ширина)
#    <img height="***px"> - размер картинки (высота)
# 10) <div></div> - блок
# 11) <input placeholder="Что ищем?"> - поле для ввода (поисковик)
#            placeholder - это атрибут для показа за текстом
# 12) <textarea></textarea> - поле для ввода большого текста
# 13) <audio controls (атрибут для появления аудио)>
#         <source src="ссылка на аудиофайл" type="тип файла (audio/mpeg)">
#     </audio>
# 14) <video></video> - для добавления видео (делайте также как и аудио)
#            Можем указать размер (также как и делали с фото)





