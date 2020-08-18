from pandas import DataFrame


def create_df(config, n):
    
    fields = config.get('fields', None)
    options = config.get("options", {})

    if not 'fields':
        raise ValueError("Config missing `fields` attribute!")
    
    # create empty dataframe
    df = DataFrame()

    if 'relations' in options:

        rel_src = [r[0] for r in options['relations']]
        rel_dest = [r[1].split('.')[0] for r in options['relations']]

        first_parent = [p for p in rel_src if p not in rel_dest][0]
        ordered_nodes = [first_parent] + [p for p in rel_src if p != first_parent] + rel_dest

        dedup_nodes = []
        for nd in ordered_nodes:
            if nd not in dedup_nodes:
                dedup_nodes.append(nd)

        ordered_fields = dedup_nodes + [f for f in fields.keys() if f not in dedup_nodes]

        # reorder the fields, so that the 'src'
        # fields are processed before the 'dest' fields
        tmp_fields = {}
        for k in ordered_fields:
            tmp_fields[k] = fields[k]

        for column_name, field in tmp_fields.items():

            if column_name in rel_dest:
                idx = rel_dest.index(column_name)
                rel = options['relations'][idx]
                df[column_name] = field.to_series(n, src=df[rel[0]], dest=rel[1].split('.')[1].lower())
            else:
                df[column_name] = field.to_series(n)
        
        # restore the original order
        df = df[list(fields.keys())]

    else:

        # append each series to the dataframe
        for column_name, field in fields.items():
            df[column_name] = field.to_series(n)

    # handle coreelation
    if 'correlation' in options:

        corr = options['correlation']

        columns = corr.columns
        fs = {k:v for k,v in fields.items() if k in columns}
        df = corr.apply_correlation(df, fs, n)

    return df