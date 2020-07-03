## Задача

- Придумать алгоритм, который сформирует замкнутый полигон по произвольному набору точек.
- Вход: набор точек в случайном порядке (dataset1.json или dataset2.json + пример визуализации Inint1.png, Inint2.png).
- Выход: набор этих же точек, образующих замкнутый полигон, содержащий все точки (Result1.png, Result2.png).
- Язык программирования Python.

___
### Решение



```
I`am use PyCharm ide
git clone https://github.com/3lement3/ViewPolygon.git
create a virtual environment
pip install -r requirements.txt
run view_polygon.py 
if terminal console run python view_polygon.py (windows) or python3 view_polygon.py if use linux
```

- метод `draw_polygon_no_verification` формирует то, что имеет json файл
- метод `draw_polygon_verification` формирует замкнутый полигон из произвольного набора точек json
- по умолчанию выставлен `draw_polygon_verification`

ps Постарался каждую строчки закоментировать своим ходом мыслей
Спасибо!!!