side_length = 7
lake_grid = [[0,0,0,0,0,0,0]
            ,[0,0,-1,0,0,0,0]
            ,[0,0,1,-1,0,-1,0]
            ,[-1,0,0,0,0,0,0]
            ,[0,0,1,0,0,1,0]
            ,[-1,0,-1,0,-1,0,0]
            ,[0,0,0,0,0,0,0]]

albert_row = 4
albert_column = 2
kuna_row = 2
kuna_column = 2

import pandas as pd
lake_data = pd.DataFrame(lake_grid)
# print(lake_data)
#

print(lake_grid[albert_column][albert_row])

for row in lake_grid:
    for column in lake_grid:
        if lake_grid[albert_column][albert_row]==1:
            safe = 'Yes'
        elif lake_grid[albert_column][albert_row] <