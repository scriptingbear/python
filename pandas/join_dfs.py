#Define a function to make it eady to join two datasets.
#Required parameters:
#left_df, right_df, left_linking_col, right_linking_col
#Optional parameters: drop_cols, sort_cols, print_report
#[11/16/2024] Now supporting {left|right|outer}
#[11/16/2024] Now supporting anti joins if optional parameter anti_join = True, default is False

def join_dfs(left_df, right_df, left_linking_col, right_linking_col, sort_cols=None, drop_cols=None, join_type='inner', anti_join=False, print_report=False):
    #Validate dataframe inputs
    dict_params = locals()
    #print(type(dict_params['left_df']).__name__)
    for param in ['left_df', 'right_df']:
        param_type = type(dict_params[param]).__name__
        if param_type != 'DataFrame':
            raise ValueError(f"parameter {param} is a {param_type}; should be a DataFrame")

    #Confirmed that first 2 parameters are dataframes. Now get the columns in
    #each one because remaining parameters are supposed to contain names
    #of existing columns.
    left_df_cols = list(left_df.columns)
    right_df_cols = list(right_df.columns)
    #Get list of distinct column names from both left and right dataframes
    all_df_cols = list(set(left_df_cols + right_df_cols))

    #Validate linking fields
    for param in ['left_linking_col', 'right_linking_col']:
        param_value = dict_params[param]
        param_type = type(param_value).__name__
        if param_type != 'str':
            raise ValueError(f"parameter {param} is a {param_type}; should be a str")

        if param == 'left_linking_col':
            if param_value not in left_df_cols:
                raise IndexError(f"parameter {param} '{param_value}' is not a valid column in left_df")
        if param == 'right_linking_col':
            if param_value not in right_df_cols:
                raise IndexError(f"parameter {param} '{param_value}' is not a valid column in right_df")

    #Validate optional parameters
    #sort_cols can be None, a string or a list of strings
    #drop_cols can be None, a string, or a list of strings
    for param in ['sort_cols', 'drop_cols']:
        param_value = dict_params[param]
        if param_value != None:
            param_type = type(param_value).__name__
            #Validate data type
            if param_type not in ['str', 'list']:
                raise ValueError(f"parameter {param} is a {param_type}; should be a str or list")

            #If passed a str, it must not be ''
            if param_type == 'str':
                if param_value.strip() == '':
                    raise ValueError(f"parameter {param} is an empty string; should be a column in either left_df and/or right_df")
                if param_value not in all_df_cols:
                    raise IndexError(f"parameter {param} '{param_value}' is not a valid column in either left_df or right_df")
            else:
                #Ensure list is not empty
                if param_value == []:
                    raise ValueError(f"parameter {param} is an empty list; should be a list of column names in either left_df and/or right_df")
                else:
                    #Ensure each value in list of column names is not ''
                    #Ensure each value in list of column names is unique
                    #Ensure each value in list of column names exists in either the left or right dataframe
                    bad_cols = [col for col in param_value if (col == '') or (param_value.count(col) > 1) or (col not in all_df_cols)]
                    if bad_cols:
                        raise ValueError(f"{param} column list {param_value} contains the following invalid columns:\n{bad_cols}")

    #Validate new join_type parameter separately
    param = 'join_type'
    param_value = dict_params[param]
    if param_value !=None:
        param_type = type(param_value).__name__
        if param_type != 'str':
            raise ValueError(f"parameter {param} is a {param_type}; should be a str")

        if param_value not in ['inner', 'left', 'right', 'outer']:
            raise ValueError(f"parameter {param} is '{param_value}'; should be either 'inner', 'left', 'right', or 'outer")


    #All inputs have been validated.
    #First get stats on left and right dfs
    left_df_row_count, left_df_col_count = left_df.shape
    right_df_row_count, right_df_col_count = right_df.shape

    try:
        #Perform the join (merge)
        #Return this merged dataframe as the last step in the function,
        #after sorting and dropping optional columns
        #Ugh! Cannot use a variable for the how= parameter.
        #Cannot coerce join_type into a string here

        #Now supporting anti joins
        if join_type == 'left':
            if anti_join:
                df_merged = pd.merge(left=left_df, right=right_df, left_on=left_linking_col, right_on=right_linking_col, how='left', indicator=True)
            else:
                df_merged = pd.merge(left=left_df, right=right_df, left_on=left_linking_col, right_on=right_linking_col, how='left')
        elif join_type == 'right':
            if anti_join:
                df_merged = pd.merge(left=left_df, right=right_df, left_on=left_linking_col, right_on=right_linking_col, how='right', indicator=True)
            else:
                df_merged = pd.merge(left=left_df, right=right_df, left_on=left_linking_col, right_on=right_linking_col, how='right')
        elif join_type == 'outer':
            df_merged = pd.merge(left=left_df, right=right_df, left_on=left_linking_col, right_on=right_linking_col, how='outer')
        elif join_type == 'inner':
            df_merged = pd.merge(left=left_df, right=right_df, left_on=left_linking_col, right_on=right_linking_col, how='inner')
        else:
            #Even though join_type was already validated, still need to provide this exit path
            #otherwise Python will complain that df_merged might potentially be "unbound".
            return None


        #If anti join specified, apply boolean mask using [_merge] to retain non matching
        #records in left df or right df. Not applicable to full outer join.
        #Drop [_merge] when done, since it should not be included in the output.

        if join_type == 'left' and anti_join:
            df_merged = df_merged[df_merged['_merge'] == 'left_only'].drop('_merge', axis=1)
        elif join_type == 'right' and anti_join:
            df_merged = df_merged[df_merged['_merge'] == 'right_only'].drop('_merge', axis=1)


        if sort_cols:
            df_merged.sort_values(sort_cols,inplace=True)

        if drop_cols:
            df_merged.drop(axis=1, labels= drop_cols, inplace=True)

        #Get final stats on merged df
        final_total_row_count, final_total_col_count = df_merged.shape

        if print_report:
            print(
                    (
                        f"left_df has {left_df_row_count:,} rows and {left_df_col_count:,} columns.\n"
                        f"right_df has {right_df_row_count:,} rows and {right_df_col_count:,} columns.\n"
                        f"Merged dataset has {final_total_row_count:,} rows and {final_total_col_count:,} columns"
                    )
                )
            df_merged.info()

    except Exception as e:
        print(f"An error occured:\n{e}")
        return None


    return df_merged
