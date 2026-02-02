import pandas as pd
import matplotlib.pyplot as plt         # bilbioteka do wykresow

df = pd.read_csv('data4.csv')

print(df)

# df.plot()                   

# plt.show()

# df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')       # scatter potrzebuje zdefiniowanego x i y,
                                                                # w poprzednim przypadku x to nr indeksu
# plt.show()

# df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

# plt.show()

df["Duration"].plot(kind = 'hist')          # histogram potrzebuje tylko 1 kolumny
                                            # wykres pokazuje, ze bylo ponad 100 treningow trwajacych ponad miedzt 50 a 60 min
plt.show()