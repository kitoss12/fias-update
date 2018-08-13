# fias-update
Python script for read XML files and update database

## Обновление таблицы addrobj

Пример файла обновления:
AS_ADDROBJ_20171117_392c8147-ac94-4308-9fe3-15d486169ec2.xml

Алгоритм обновления:
1) Если элемент с конкретным aoid присутствует в таблице, то происходит обновление строки
2) Если элемент с конкретным aoid отсутствует, то добавляется новая запись в таблицу
3) Удаляются нерелевентные данные (WHERE livestatus != 1 AND currstatus != 0)

Запуск:
```
python .\addrobj.py .\AS_ADDROBJ_20171117_392c8147-ac94-4308-9fe3-15d486169ec2.XML -n fias -a 192.168.1.1 -u admin -s mypassword
```

Для получения справки можно воспользоваться командой:
```
python .\addrobj.py --help
```

### Удаление технологически удаленных данных

При наличии файла AS_DEL_ADDROBJ*.xml требуется запускать скрипт:
```
python .\del_addrobj.py .\AS_DEL_ADDROBJ_20171228_64fe4ec0-2e67-41b9-8335-b139a665b173.XML -n fias -a 192.168.1.1 -u admin -s mypassword
```

## Обновление таблицы socrbase

Пример файла обновления:
AS_SOCRBASE_20171117_31f99a0d-6be2-4e39-a73e-f8a544f96174.xml

Алгоритм обновления:
1) Происходит удаление всех записей из таблицы socrbase
2) Происходит чтение xml файла и последовательное заполнение таблицы socrbase

Запуск:
```
python .\socrbase.py .\AS_SOCRBASE_20171117_31f99a0d-6be2-4e39-a73e-f8a544f96174.XML -n fias -a 192.168.1.1 -u admin -s mypassword
```


Для получения справки можно воспользоваться командой:
```
python .\socrbase.py --help
```
