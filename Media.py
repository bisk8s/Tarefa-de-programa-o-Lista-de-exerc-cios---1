# -*- coding: utf-8 -*-
notas = []
notas.append(float(input('Digite a primeira nota:')))
notas.append(float(input('Digite a segunda nota:')))
notas.append(float(input('Digite a terceira nota:')))
notas.append(float(input('Digite a quarta nota:')))

print('A média aritmética é', float(sum(notas))/len(notas))