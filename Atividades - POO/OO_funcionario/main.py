"""
Fazer um programa para ler os dados de um funcionário (nome, salário bruto e imposto). Em
seguida, mostrar os dados do funcionário (nome e salário líquido). Em seguida, aumentar o
salário do funcionário com base em uma porcentagem dada (somente o salário bruto é
afetado pela porcentagem) e mostrar novamente os dados do funcionário. Use a classe
projetada abaixo.
"""
from employee import Employee

name = input('Name: ')
gs = float(input('Gross salary: '))
tax = float(input('Tax: '))

trabalhador = Employee(name, gs, tax)

print(f'Employee: {trabalhador.update()}')
percentage = float(input('Which percentage to increase salary? '))
trabalhador.increase_salary(percentage)
print(f'Updated data: {trabalhador.update()}')