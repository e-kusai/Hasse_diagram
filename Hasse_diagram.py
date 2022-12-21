#������ - ����������� ��������� ����� ��� ��������� ��������� ����� N � ������������ ���������� ��������� 

import networkx as nx
import matplotlib.pyplot as plt

# 1. ������� ������ � ��������� ��� ���������� ����� 60
n_lst=[]
def create_nodes_list(lst, value):
  for i in range(1, int(value/2)+1):
    if value%i ==0:
      lst.append(i)
  lst.append(value)

create_nodes_list(n_lst, 60)
#print(n_lst)

# 2. �������, ������� ���������, ���� �� � ������ �������� ������� �����. ���� ���� - ������ ���, ���� ��� - ����
def check_el(el, lst):
  for e in lst:
    if el%e == 0:
      return True
  return False

# 3. ���������� �� ������� � ���� ������  - ��������� ��� ������, ���� �� � ��� �������� ������ ��������. ���� � ������� ������ (������) ���� �������� ������� ��-�� - �������� �� ������� ����. ���� ��� - ��������� ��-� � ������ ������� � ������� �� �����
def find_level(el, lst_lev):
  for l in lst_lev:
    if check_el(el, l):
      pass
    else:
      l.append(el)
      break

# 4. ������� ������ � �������� (������� - ������ �����)
def set_levels(lst):
  levels=[[1]] #������� ������ �������, �� ������ ������ ������ ����� ����� 1,� ������ ���, ��� ��� ������ ������� - ��������� �����
  #�������� ������ �� ���� ��������� ����� 60 - ���� ������������ �� �� �������
  for i in range (1, len(lst)):
    lev_n=len(levels) #�� ������ ���� �������� ������� ���-�� �������
    
    #���������, ���� �� �� ������� ������� ������ �������� ������� ��������. ���� ���� - ��������� ����� ������� � ��-� ���������� ����.
    if check_el(lst[i], levels[lev_n-1]):
      if lev_n==len(levels):
        levels.append([])
      levels[lev_n].append(lst[i])

      #���� �� ������� ������� ������ �������� ����� ��� - ���������� �� ���� ���������� �������, ����� �����, ��� ������ ���� ������ ��-�, �.�. ���������, ��� ��������� ��������� �������, ���������� �������� ������� ��������, � ���������� ��-� �� ������� ����
    else:
      find_level(lst[i], levels)
      
  return levels #�-� ���������� ������ ������� � ������������� �� ��� ����������, ����� �� ������ ���� �������� ���� � ����� ����� ������

lvls=set_levels(n_lst)
#print(lvls)

def make_nodes(lst_lev, gr):
  gr.add_node(lst_lev[0][0])
  for i in range(1, len(lst_lev)): #���������� �� �������
    for el in lst_lev[i]: #�������� �� ��������� �� ������
      gr.add_node(el) #������� ���� � ����� ������
      for el_prev in lst_lev[i-1]:
        if el%el_prev==0:
          gr.add_edge(el, el_prev)
          
#������� ����������� ������������ �����    
def make_pos(lvls):
  pos={}
  for i in range(len(lvls)): #���������� �� �������, i - ����� ������. ��� ���������� �� �
    for j in range(len(lvls[i])):
      x=len(lvls[i])/2-j #������ ����� ���� �������� ������������ �� �, � ��  � ������� � ������������ ������
      pos[lvls[i][j]]=[x,i] #���������� ����� ������ 
  return(pos)

pos=make_pos(lvls)

H=nx.Graph()
make_nodes(lvls, H)

nx.draw(H, with_labels=True, font_weight='bold', pos=pos)
plt.show()
