import sys
import pandas as pd

fname = sys.argv[1]

df = pd.read_csv(fname, sep="\t", header=None)
nsamples = len(df.columns)-1
cols = ["s"+str(i) for i in range(1,nsamples+1)]
cols.insert(0,"gname")
df.columns = cols
df = df.drop(cols[-1], axis=1)
print(df)
fout = fname.split(".")[0] + ".expr.tsv"
df.to_csv(fout, sep="\t", index=False)