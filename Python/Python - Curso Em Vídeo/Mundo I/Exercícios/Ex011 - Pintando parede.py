a=float(input('Digite a altura da perede: '))
l=float(input('Digite a largura da parede: '))
p=float(a*l)
r=p/2
print('A sua parede tem a dimesão de {} x {:.2f} possui a área de {:.2f}'.format(a,l,p))
print('Para pinta essa parede você precisará de ',(r), ' litros de tinta')