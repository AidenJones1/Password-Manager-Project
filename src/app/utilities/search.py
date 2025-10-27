from ..table.table import AccountsTable

def perform_search(query: str):
    """Search the DataFrame for any cell that contains what is specified in the query.""" 
    df = AccountsTable().get_df().copy()

    if not query:
        return df
    
    mask = df.apply(lambda row: row.astype(str).str.contains(query).any(), axis=1)
    results_df = df.loc[mask].reset_index(drop = True).copy()

    return results_df