def clean_split_lines(lines):
    """
    Cleans the list of any entries that are nothing by white-space
    """
    return [
        line.rstrip().lstrip()
            for line in lines if len(line.rstrip().lstrip()) != 0
    ]