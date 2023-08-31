from matplotlib import pyplot as plt

plt.text(0.01, 0.9, "У нас корзина с 15 мячами, 9 новых", fontsize=15)
plt.text(0.01, 0.8, "и 6 старых. Взяли 3 мяча, поиграли и", fontsize=15)
plt.text(0.01, 0.7, "вернули обратно. Расчитать вероятность", fontsize=15)
plt.text(0.01, 0.6, "что вследующий раз 3 взятых мяча", fontsize=15)
plt.text(0.01, 0.5, "будут новыми.", fontsize=15)
plt.text(0.01, 0.4, "Используем формулы:", fontsize=15)
form = r"$C_n^k = \frac{n!}{k!(n-k)!} ; P(A_i)=\frac{n_i}{N} ; P(B) = \sum_{i=1}^3 P(B|A_i)P(A_i)$"
plt.text(0.01, 0.3, form, fontsize=15)
form = r"$P(B|A_i) = p_i; P(A_i|B) = \frac{P(B|A_i)P(A_i)}{P(B)}$"
plt.text(0.01, 0.1, form, fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, "Решение:", fontsize=15)
plt.text(0.01, 0.8, "1) Вероятность что 3 мяча будут старыми:", fontsize=15)
form = r"$P(H_1) = \frac{C_9^3}{C_{15}^3} = \frac{84}{455}$"
plt.text(0.01, 0.7, form, fontsize=15)
plt.text(0.01, 0.6, "2) 2 старых и 1 новый:", fontsize=15)
form = r"$P(H_2) = \frac{C_9^3*C_6^1}{C_{15}^3} = \frac{216}{455}$"
plt.text(0.01, 0.5, form, fontsize=15)
plt.text(0.01, 0.4, "3) 1 старый и 2 новых:", fontsize=15)
form = r"$P(H_3) = \frac{C_9^1*C_6^2}{C_{15}^3} = \frac{135}{455}$"
plt.text(0.01, 0.3, form, fontsize=15)
plt.text(0.01, 0.2, "4) все 3 мяча новые:", fontsize=15)
form = r"$P(H_4) = \frac{C_6^3}{C_{15}^3} = \frac{20}{455}$"
plt.text(0.01, 0.1, form, fontsize=15)


fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, "Далее рассмотрим разное кол. новых мячей:", fontsize=15)
plt.text(0.01, 0.8, "1) Вероятность что 6 новых мячей:", fontsize=15)
form = r"$P(A|H_1) = \frac{C_6^3}{C_{15}^3} = \frac{20}{455}$"
plt.text(0.01, 0.7, form, fontsize=15)
plt.text(0.01, 0.6, "2) Вероятность что 7 новых мячей:", fontsize=15)
form = r"$P(A|H_2) = \frac{C_7^3}{C_{15}^3} = \frac{35}{455}$"
plt.text(0.01, 0.5, form, fontsize=15)
plt.text(0.01, 0.4, "3) Вероятность что 8 новых мячей:", fontsize=15)
form = r"$P(A|H_3) = \frac{C_8^3}{C_{15}^3} = \frac{56}{455}$"
plt.text(0.01, 0.3, form, fontsize=15)
plt.text(0.01, 0.2, "4) Вероятность что 9 новых мячей:", fontsize=15)
form = r"$P(A|H_4) = \frac{C_9^3}{C_{15}^3} = \frac{84}{455}$"
plt.text(0.01, 0.1, form, fontsize=15)


fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, "Ну а теперь общая вероятность события:", fontsize=15)
form = r"$P(A) = \frac{20}{455}*\frac{84}{455} + \frac{35}{455}*\frac{216}{455} + \frac{56}{455}*\frac{135}{455} + \frac{84}{455}*\frac{20}{455} = $"
plt.text(0.01, 0.7, form, fontsize=15)
form = r"$= \frac{48}{5915} + \frac{216}{5915} + \frac{216}{5915} + \frac{48}{5915} =$"
plt.text(0.01, 0.5, form, fontsize=15)
form = r"$= \frac{528}{5915} = 0,0892 * 100 = $"
plt.text(0.01, 0.3, form, fontsize=15)
plt.text(0.01, 0.1, "Вероятность = 8,92 %", fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()