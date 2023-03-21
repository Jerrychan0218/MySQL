import pandas as pd
hi = pd.merge_ordered(a, b, on = variance, suffixes = ('_a','_b'))