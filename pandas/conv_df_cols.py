def conv_df_cols(df, col_conv_specs):
    if type(df).__name__ != 'DataFrame':
        raise TypeError("df parameter is not a DataFrame")

    if type(col_conv_specs).__name__ != 'dict':
        raise TypeError("col_conv_specs parameter is not a dictionary")
    
    if len(col_conv_specs) == 0:
        raise ValueError("col_conv_specs parameter is an empty dict")

    #Get names of columns in dataframe
    df_cols = list(df.columns)
    #Validate input
    bad_cols = []
    for col in col_conv_specs:
        if col not in df_cols:
            bad_cols.append(col)
    if bad_cols != []:
        print(f"The following columns do not exist in the dataframe:\n{bad_cols}")
        return
    
    #Specify valid data conversion types
    valid_data_types = ['string', 'numeric', 'datetime']

    for data_type in col_conv_specs.values():
        bad_data_types = []
        if data_type not in valid_data_types:
            bad_data_types.append(data_type)
        if bad_data_types !=[]:
            print(f"Invalid data conversion specifications:\n{bad_data_types}")
            return

    #Create string variable to hold stats report
    stats_report = ""

    #Convert each specified column to the specified data type
    for col, col_data_type in col_conv_specs.items():
        #Get column as a series
        col_as_series = df[col]
        #Convert as specified
        #For numeric and datatime, need to coerce bad values
        #to NaN

        if col_data_type == 'numeric':
            col_as_series_conv = pd.to_numeric(col_as_series,errors='coerce')
      
        elif col_data_type == 'datetime':
            col_as_series_conv = pd.to_datetime(col_as_series,errors='coerce')

        elif col_data_type == 'string':
            col_as_series_conv = col_as_series.to_string()
        
        #Replace existing column in dataframe
        df[col] = col_as_series_conv

        #Get the indexes of NaN values in the series
        #Does not apply to string (object) columns
        if col_data_type in ['numeric', 'datetime']:
            col_errs = col_as_series_conv[col_as_series_conv.isna()]

            #Get a list of the indexes of the first 10 bad items in
            #the series (dataframe column) and the bad values themselves
            err_index_list = list(dict(col_errs.head(10)).keys())
            if err_index_list != []:
                err_info = {item: col_as_series.iloc[item] for item in err_index_list}
                #print dictionary with one entry per line for easier reading
                pretty_err_info = "\n".join([f"{key}: {value}" for key, value in err_info.items()])
                stats_report += f"Indexes of first 10 bad values in col [{col}]:\n{pretty_err_info}\n\n"

    #Include info about the updated dataframe in stats report
    print(stats_report)
    print("_" * 20)
    print(df.info())
        





    