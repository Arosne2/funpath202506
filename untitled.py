import pandas as pd

def switch_accessions_with_entries(accession_list, df):
    """
    Takes a list of accession IDs and switches them with corresponding Entry values from a DataFrame.
    
    Parameters:
    accession_list (str or list): Either a string of space-separated accession IDs or a list of accession IDs
    df (pd.DataFrame): DataFrame with 'Accession' and 'Entry' columns
    
    Returns:
    list: List of Entry values corresponding to the input accession IDs
    """
    
    # Handle string input by splitting on whitespace
    if isinstance(accession_list, str):
        accessions = accession_list.split()
    else:
        accessions = accession_list
    
    # Create a mapping dictionary from the DataFrame
    accession_to_entry = dict(zip(df['Accession'], df['Entry']))
    
    # Switch accessions to entries
    switched_entries = []
    not_found = []
    
    for acc in accessions:
        acc = acc.strip()  # Remove any extra whitespace
        if acc in accession_to_entry:
            switched_entries.append(accession_to_entry[acc])
        else:
            not_found.append(acc)
            switched_entries.append(None)  # or you could skip these entirely
    
    # Print warning for any accessions not found
    if not_found:
        print(f"Warning: The following accessions were not found in the DataFrame: {not_found}")
    
    return switched_entries