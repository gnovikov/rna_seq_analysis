def signature(rawcount_dataframe, method, experimental_samples, control_samples, constant_threshold=10**-5):


        # Connect to R
        from rpy2.robjects import r, pandas2ri
        import pandas as pd
        import sys
 
        pandas2ri.activate()

        # Create design dict
        sample_dict = {'experimental': experimental_samples, 'control': control_samples}

        # Create design dataframe
        design_dataframe = pd.DataFrame({group_label: {sample:int(sample in group_samples) for sample in rawcount_dataframe.columns} for group_label, group_samples in sample_dict.iteritems()})

        # Convert to R
        rawcount_dataframe_r = pandas2ri.py2ri(rawcount_dataframe)
        design_dataframe_r = pandas2ri.py2ri(design_dataframe)

        # Run
        if method == 'CD':
            signature_dataframe_r = r.run_characteristic_direction(rawcount_dataframe_r, design_dataframe_r, constant_threshold)
        elif method == 'limma':
            signature_dataframe_r = r.run_limma(rawcount_dataframe_r, design_dataframe_r)
        else:
            raise ValueError('Wrong method supplied.  Must be limma or CD.')

        # Convert to pandas and sort
        signature_dataframe = pandas2ri.ri2py(signature_dataframe_r)

        # Add
   
        return signature_dataframe

