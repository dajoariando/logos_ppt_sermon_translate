def parse_txt(file_path):
    """
    Reads a text file and returns its contents as a list of non-empty, stripped lines.

    :param file_path: Path to the text file
    :return: List of non-empty, stripped lines from the text file
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line.strip()]