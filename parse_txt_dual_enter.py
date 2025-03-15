def parse_txt_dual_enter(file_path):
    """
    Reads a text file and returns its contents as a list of non-empty, stripped blocks of text,
    separated by double newline characters.

    :param file_path: Path to the text file
    :return: List of non-empty, stripped blocks of text from the text file
    """
    with open(file_path, 'r') as file:
        content = file.read()
    blocks = content.split('\n\n')
    return [block.strip() for block in blocks if block.strip()]

# Example usage:
# file_path = '/media/dave/SSD1T_AORUS/vm_share/WORKSPACES/Python/Sermon_translate/path_to_your_file.txt'
# blocks_list = parse_txt_dual_enter(file_path)
# print(blocks_list)