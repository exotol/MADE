# Базовая вычислительная геометрия

## A. Принадлежность точки отрезку

Ограничение по времени на тест: 2 секунды

Ограничение по памяти на тест: 256 мегабайт

ввод: стандартный ввод

вывод: стандартный вывод

### Входные данные

Шесть чисел — координаты точки и координаты концов отрезка.

### Выходные данные

Одна строка YES, если точка принадлежит отрезку, и NO в противном случае.

### Примеры

**Входные данные**
```
3 3 1 2 5 4
```

**Выходные данные**
```
YES
```

**Входные данные**
```
4 2 4 2 4 5
```

**Выходные данные**
```
YES
```

### [Решение](taskA.py)

## B. Пересечение двух отрезков

Ограничение по времени на тест: 1 секунда

Ограничение по памяти на тест: 256 мегабайт

ввод: стандартный ввод

вывод: стандартный вывод

Необходимо проверить, пересекаются ли два отрезка.

### Входные данные

В двух строках входного файла заданы по четыре целых числа, не превосходящих по модулю 10000, — координаты концов
первого отрезка, затем второго. 

### Выходные данные

В первой строке выходного файла выведите «YES», если отрезки имеют общие точки, и «NO» в противном случае.

### Пример

**Входные данные**
```
5 1 2 6
1 1 7 8
```

**Выходные данные**
```
YES
```

### [Решение](taskB.py)

## C. Точка в многоугольнике

Ограничение по времени на тест: 1 секунда

Ограничение по памяти на тест: 256 мегабайт

ввод: стандартный ввод

вывод: стандартный вывод

### Входные данные

В первой строке содержится три числа —– _N_ (3⩽ _N_ ⩽100000) и координаты точки. Последующие _N_ строк содержат
координаты углов многоугольника. Координаты — целые, не превосходят 10^6 по модулю.

### Выходные данные

Одна строка YES, если заданная точка содержится в приведённом многоугольнике или на его границе, и NO в
противном случае.

### Пример

**Входные данные**
```
3 2 3
1 1
10 2
2 8
```

**Выходные данные**
```
YES
```

### [Решение](taskC.py)

## D. Площадь многоугольника

Ограничение по времени на тест: 2 секунды

Ограничение по памяти на тест: 256 мегабайт

ввод: стандартный ввод

вывод: стандартный вывод

### Входные данные

В первой строке одно число _N_ ({3 ≤ _N_ ≤ 100 000}). Далее в _N_ строках по паре чисел –— координаты очередной
вершины простого многоугольника в порядке обхода по или против часовой стрелки.

Все координаты — целые числа, по модулю не превосходящие 10^4.

### Выходные данные

Одно число —– величина площади приведённого многоугольника.

### Пример

**Входные данные**
```
3
1 0
0 1
1 1
```

**Выходные данные**
```
0.5
```

### [Решение](taskD.py)

## E. Периметр выпуклой оболочки

Ограничение по времени на тест: 2 секунды

Ограничение по памяти на тест: 256 мегабайт

ввод: стандартный ввод

вывод: стандартный вывод

Дано _N_ точек на плоскости.

Нужно вычислить периметр выпуклой оболочки данных точек.

Гарантируется, что выпуклая оболочка не вырождена.

### Входные данные

В первой строке число _N_ (3 ≤ _N_ ≤ 10^5). Следующие _N_ строк содержат пары целых чисел _x_ и _y_
( - 10^9 ≤ _x, y_ ≤ 10^9) — точки.

Будьте аккуратны! Точки произвольны. Бывают совпадающие, бывают лежащие на одной прямой в большом количестве.

### Выходные данные

Одно вещественное число — периметр выпуклой оболочки. Выводите число с максимально возможной точностью.

### Пример

**Входные данные**
```
5
0 0
2 0
0 2
1 1
2 2
```

**Выходные данные**
```
8
```

### [Решение](taskE.py)
