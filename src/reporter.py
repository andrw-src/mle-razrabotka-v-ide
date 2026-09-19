import pandas as pd

class DataFrameReporter:
    def __init__(self, float_format = '0.05f', percent_format = '0.02%', include_all = False):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all

    def show_report(self, df, title=None):
        if title:
            print(title)
    
        print('Количество столбцов:', df.shape[1])
        print('Количество строк:', df.shape[0])

        duplicates = df.duplicated().sum()
        print('Количество дубликатов:', duplicates)

        print('Доля дубликатов:', format(duplicates / df.shape[0], self.percent_format))

import pandas as pd

data = pd.read_csv('/Users/andrew/Practikum/mle-razrabotka-v-ide/data/payments.csv')

reporter_1 = DataFrameReporter(float_format='0.02f', percent_format='0.03%')
reporter_2 = DataFrameReporter(float_format='0.03f', percent_format='0.01%', include_all=True)

reporter_1.show_report(data, 'Отчёт в формате 1:')
print()
reporter_2.show_report(data, 'Отчёт в формате 2:')

# вызови метод show_report для reporter, передав в него датафрейм
#reporter_1.show_report(data)
#reporter_2.show_report(data) 