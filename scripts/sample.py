from pandas import read_csv


files = ["deprecated_libraries", "explicit_mention"]

zVal = 1.96
for filename in files:
    # read the data
    filepath = "data/filtered/"+filename+".csv" 
    df = read_csv(filepath)
    
    # calculate a 95% confidence interval
    pop = len(df.index)
    conInt = 5
    ss = ((zVal * zVal) * 0.25) / ((conInt / 100) * (conInt / 100))
    ss = ss / (1 + (ss - 1) / pop)
    n = int(ss+.5)
    
    sample = df.sample(n=n, replace=False)
    print('\nPop: %d, 95 conf: %d' % (pop, n))
    filepath = "data/filtered/"+filename+"_sample.csv"
    sample.to_csv(filepath)
