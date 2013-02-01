def clean_split_lines(lines):
    return [
        line.rstrip().lstrip()
            for line in lines if len(line.rstrip().lstrip()) != 0
    ]