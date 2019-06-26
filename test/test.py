import pandas as pd

if __name__ == '__main__':
    left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                         'A': ['A0', 'A1', 'A2', 'A3'],
                         'B': ['B0', 'B1', 'B2', 'B3']})
    print(left)
    print(left['key'])
    print(left['key'].unique())

