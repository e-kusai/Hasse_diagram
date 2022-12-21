#Задача - составление диаграммы Хассе для делителей заданного числа N и визуализация полученной диаграммы 

import networkx as nx
import matplotlib.pyplot as plt


n=60
# 1. Создаем список и заполняем его делителями числа 60
n_lst=[]
def create_nodes_list(lst, value):
  for i in range(1, int(value/2)+1):
    if value%i ==0:
      lst.append(i)
  lst.append(value)

create_nodes_list(n_lst, n)
#print(n_lst)

# 2. Функция, которая проверяет, есть ли в списке делители данного числа. Если есть - вернет ТРУ, если нет - ФОЛС
def check_el(el, lst):
  for e in lst:
    if el%e == 0:
      return True
  return False

# 3. Проходимся по уровням и ищем нужный  - проверяем все уровни, есть ли в них делитель нашего элемента. Если в текущем уровне (списке) есть делитель данного эл-та - движемся на уровень выше. Если нет - добавляем эл-т в данный уровень и выходим из цикла
def find_level(el, lst_lev):
  for l in lst_lev:
    if check_el(el, l):
      pass
    else:
      l.append(el)
      break

# 4. Создаем список с уровнями (уровень - список чисел)
def set_levels(lst):
  levels=[[1]] #создаем список уровней, на нижнем уровне всегда будет число 1,и только оно, так что нижний уровень - отправная точка
  #ПРоходим циклом по всем делителям числа 60 - чтоб распределить их по уровням
  for i in range (1, len(lst)):
    lev_n=len(levels) #на каждом шаге измеряем текущее кол-во уровней
    
    #проверяем, есть ли на текущем верхнем уровне делитель данного элемента. Если есть - добавляем новый уровень и эл-т записываем туда.
    if check_el(lst[i], levels[lev_n-1]):
      if lev_n==len(levels):
        levels.append([])
      levels[lev_n].append(lst[i])

      #Если на текущем верхнем уровне делителя числа нет - проходимся по всем предыдущим уровням, чтобы найти, где должен быть данный эл-т, т.е. проверяем, где находится последний уровень, содержащий делитель данного элемента, и записываем эл-т на уровень выше
    else:
      find_level(lst[i], levels)
      
  return levels #ф-я возвращает список уровней с содержащимися на них элементами, далее на основе него построим узлы и связи между узлами

lvls=set_levels(n_lst)
#print(lvls)

def make_nodes(lst_lev, gr):
  gr.add_node(lst_lev[0][0])
  for i in range(1, len(lst_lev)): #проходимся по уровням
    for el in lst_lev[i]: #проходим по элементам из уровня
      gr.add_node(el) #создаем узел в любом случае
      for el_prev in lst_lev[i-1]:
        if el%el_prev==0:
          gr.add_edge(el, el_prev)
          
#задание корректного расположения узлов    
def make_pos(lvls):
  pos={}
  for i in range(len(lvls)): #проходимся по уровням, i - номер уровня. Это координата по У
    for j in range(len(lvls[i])):
      x=len(lvls[i])/2-j #делаем чтобы было красивое расположение по Х, а не  в столбик с разрастанием вправо
      pos[lvls[i][j]]=[x,i] #координаты точки задаем 
  return(pos)

pos=make_pos(lvls)

H=nx.Graph()
make_nodes(lvls, H)

nx.draw(H, with_labels=True, font_weight='bold', pos=pos)
plt.show()
