Много времени потратил на то, чтобы дописать получение меток для картинок,
 и в итоге не успел придумать ничего лучше решения, которое было готово в течение первых пары дней

С попыткой решения с картинками можно ознакомиться в файле kaggle_kazan-express-testovoe.ipynb
 Там есть и заметки о том, что что делает, и какие-то записи полученных метрик
 Лучшим результатом на валидации во время обучения по f1 оказался 0.36
 Применить его каким-либо образом я не сумел
 Думаю дело в том, что мало картинок на класс
 И некоторые картинки сложно применимы (часть одежды с фото в полный рост)

Оттуда же я адаптировал и использовал ограничение по количеству объектов одного класса,
 в уже ставшим основным, файле Kazan_exp
 они, впрочем, на финальный ответ тоже не повлияли

Файл выглядит достаточно хаотичным, хоть я и попытался его причесать
 Воспроисводимость должна быть на месте

На нейронке или катбусте в 1000 итераций сохранил бы веса/модели,
 Но тут достаточно быстро все считается

Не хватило времени

Спасибо за тестовое, потрогал штуки, которые раньше не трогал
И получил опыт