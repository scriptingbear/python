def update_df_cols(dframe, rename_info):
    #Method expects to receive a dataframe object, which is mutable,
    #and a list of original column names and new column names, e.g.
    #update_columns(my_df, []"org_col1_name", "new_col1_name", "org_col2_name",
    #new_col2_name", ...])
    #[11/16/2024] Changed name from update_columns to update_df_cols.
    #[11/16/2024] Changes *args parameter to rename_info: list


    #****************************************
    #Validate inputs
    #****************************************
    if type(dframe).__name__ != 'DataFrame':
        raise ValueError("dframe argument is not a dataframe")

    #rename_info must be a list, not hard coded values separated by commas.

    param_type = type(rename_info).__name__
    if param_type != 'list':
        raise ValueError(f"parameter rename_info is a {param_type}; should be a list")

    #Make sure you have a "list" of column names to work with
    if len(rename_info) == 0:
        raise ValueError("no columns specified")

    #Each original column name must be paired with a new column name
    if len(rename_info) % 2 != 0:
        print(f"len(rename_info) = {len(rename_info)}")
        print(f"len(rename_info) % 2 = {len(rename_info) % 2 }")
        raise ValueError("column list does not have an even number of items")

    #Each element in rename_info must be a string
    for idx, item in enumerate(rename_info):
        item_type = type(item).__name__
        if item_type != 'str':
            raise ValueError(f"rename[{idx}] is a {item_type}; should be a str")


    #Can't have any "" in column list
    for item in rename_info:
        if item.strip() == "":
            raise ValueError("zero length string or blank items in column list")



    #****************************************
    #Update the names of columns if they exist in the dataframe.
    #Track invalid column names and display a report if necessary
    #****************************************
    bad_col_names = []
    org_col_names = rename_info[::2]

    bad_rename_cols = []
    rename_cols = rename_info[1::2]

    for col_name in org_col_names:
        if col_name not in dframe.columns:
            bad_col_names.append(col_name)

    #Stop if invalid original columns were specified
    if bad_col_names:
        raise IndexError(f"The following columns do not exist in the specified dataframe:\n{bad_col_names}")

    #Can't rename a column to the name of an existing column
    for col_name in rename_cols:
        if col_name in dframe.columns:
            bad_rename_cols.append(col_name)

    #Stop if renamed column conflicts with existing column name
    if bad_rename_cols:
        raise IndexError(f"The following columns already exist in the specified dataframe:\n{bad_rename_cols}")


    #The dataframe columns property expects a dictionary of old and
    #new column names
    col_update_specs = {}
    for col_name in org_col_names:
        if col_name not in bad_col_names:
            #Need postion of the next element, which is the updated
            #column name
            new_col_name_loc = rename_info.index(col_name) + 1
            new_col_name = rename_info[new_col_name_loc]
            col_update_specs[col_name] = new_col_name

    #Ready to update the dataframe
    dframe.rename(columns = col_update_specs, inplace=True)
    print(f"Dataframe has been updated:\n{list(dframe.columns)}")
   




