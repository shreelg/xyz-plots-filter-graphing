import pandas as pd

def org(input_file):
    
    df = pd.read_csv(input_file)

    
    first_column = df.iloc[:, 0]
   
    pattern_length = 3

    totalPatterns = len(first_column) // pattern_length

    
    remaining_elements = len(first_column) % pattern_length
    organized_data = {'x': [], 'y': [], 'z': []}


    for i in range(totalPatterns):
        organized_data['x'].append(first_column.iloc[i * pattern_length])
        organized_data['y'].append(first_column.iloc[i * pattern_length + 1])
        organized_data['z'].append(first_column.iloc[i * pattern_length + 2])


    for i in range(remaining_elements):
        organized_data[['x', 'y', 'z'][i]].append(first_column.iloc[totalPatterns * pattern_length + i])

    organized_df = pd.DataFrame(organized_data)
     
    organized_df.to_csv('name of output csv', index=False)


org('path of source csv')
