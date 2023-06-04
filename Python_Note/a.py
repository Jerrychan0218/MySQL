import pandas as pd
import numpy as np
a = [1,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3]
a = pd.DataFrame(a)
print(a.mode())