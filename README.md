# D_news
d2
Модель Author
Модель, содержащая объекты всех авторов.
Имеет следующие поля:
cвязь «один к одному» с встроенной моделью пользователей User;
рейтинг пользователя. Ниже будет дано описание того, как этот рейтинг можно посчитать.
Модель Category
Категории новостей/статей — темы, которые они отражают (спорт, политика, образование и т. д.). Имеет единственное поле: название категории. Поле должно быть уникальным (в определении поля необходимо написать параметр unique = True).
Модель Post
Эта модель должна содержать в себе статьи и новости, которые создают пользователи. Каждый объект может иметь одну или несколько категорий.
Соответственно, модель должна включать следующие поля:
связь «один ко многим» с моделью Author;
поле с выбором — «статья» или «новость»;
автоматически добавляемая дата и время создания;
связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory);
заголовок статьи/новости;
текст статьи/новости;
рейтинг статьи/новости.
Модель PostCategory
Промежуточная модель для связи «многие ко многим»:
связь «один ко многим» с моделью Post;
связь «один ко многим» с моделью Category.
Модель Comment
Под каждой новостью/статьёй можно оставлять комментарии, поэтому необходимо организовать их способ хранения тоже.
Модель будет иметь следующие поля:
связь «один ко многим» с моделью Post;
связь «один ко многим» со встроенной моделью User (комментарии может оставить любой пользователь, необязательно автор);
текст комментария;
дата и время создания комментария;
рейтинг комментария.

d3
Создать новую страницу с адресом /news/, на которой должен выводиться список всех новостей.
Вывести все статьи в виде заголовка, даты публикации и первых 20 символов текста.
Новости должны выводиться в порядке от более свежей к самой старой.
Сделать отдельную страницу для полной информации о статье /news/<id новости>.
На этой странице должна быть вся информация о статье. Название, текст и дата загрузки в формате день.месяц.год.

Написать собственный фильтр censor, который заменяет буквы нежелательных слов в заголовках и текстах статей на символ «*».

Все новые страницы должны использовать шаблон default.html как основу.

d4 
Добавьте постраничный вывод на /news/, чтобы на одной странице было не больше 10 новостей и видны номера лишь ближайших страниц, а также возможность перехода к первой или последней странице.
Добавьте страницу /news/search. На ней должна быть реализована возможность искать новости по определённым критериям. Критерии должны быть следующие:
по названию;
по категории;
позже указываемой даты.
Убедитесь, что можно выполнить фильтрацию сразу по нескольким критериям
Запрограммируйте страницы создания, редактирования и удаления новостей и статей. Предлагаем вам расположить страницы по следующим ссылкам:
/news/create/
/news/<int:pk>/edit/
/news/<int:pk>/delete/
/articles/create/
/articles/<int:pk>/edit/
/articles/<int:pk>/delete/
/articles/<int:pk>/delete/

d5 Добавьте форму регистрации на сайте с возможностью зарегистрироваться с помощью почты и пароля или через Yandex-аккаунт. Для этого используйте пакет django-allauth. После того как пользователь войдёт, его должно перенаправить на страницу с новостями.
Настройте проверки у представлений создания и редактирования новостей и статей. Создайте группу authors, выдайте ей права на создание и изменение новых записей в разделах «Статьи» и «Новости».
Проверьте работу прав.


d6В категории должна быть возможность пользователей подписываться на рассылку новых статей.
Если пользователь подписан на какую-либо категорию, то, как только в неё добавляется новая статья, её краткое содержание приходит пользователю на электронную почту, которую он указал при регистрации. В письме обязательно должна быть гиперссылка на саму статью, чтобы он мог по клику перейти и прочитать её.
Если пользователь подписан на какую-либо категорию, то каждую неделю ему приходит на почту список новых статей, появившийся за неделю с гиперссылкой на них, чтобы пользователь мог перейти и прочесть любую из статей.
Добавьте приветственное письмо пользователю при регистрации в приложении.

7.5
Установить Redis
Установить Celery
Произвести необходимые конфигурации Django для соединения всех компонент системы.
Реализовать рассылку уведомлений подписчикам после создания новости.
Реализовать еженедельную рассылку с последними новостями (каждый понедельник в 8:00 утра)
