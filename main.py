import zipfile
import os
import shutil


def clear_directory(directory):
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if item != '.gitkeep':
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)


def extract_zip(zip_path, extract_to="."):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        return zip_ref.namelist()


def generate_tree(directory, prefix=''):
    tree_str = ""
    files = sorted(os.listdir(directory))
    for i, file in enumerate(files):
        path = os.path.join(directory, file)
        is_last = i == (len(files) - 1)
        tree_str += prefix + ("└── " if is_last else "├── ") + file + "\n"
        if os.path.isdir(path):
            extension = "    " if is_last else "│   "
            tree_str += generate_tree(path, prefix=prefix + extension)
    return tree_str


def read_prologue_file(prologue_file_path):
    """Read the contents of the prologue file.

    Args:
        prologue_file_path (str): Path to the prologue file.

    Returns:
        str: The contents of the prologue file.
    """
    try:
        with open(prologue_file_path, 'r', encoding='utf-8') as prologue_file:
            return prologue_file.read() + "\n\n"
    except FileNotFoundError:
        return ""


def write_tree_and_contents(
        zip_contents,
        extract_to,
        output_file,
        prologue_content
):
    """Write the directory tree and file contents to an output file.

    Args:
        zip_contents (list): List of file paths from the ZIP.
        extract_to (str): Directory where the ZIP contents are extracted.
        output_file (str): Path to the output file.
        prologue_content (str): Content to be written as a prologue.
    """
    with open(output_file, "w", encoding="utf-8") as f:
        # Write the prologue content
        f.write(prologue_content)

        # Write the tree structure
        f.write(generate_tree(extract_to))
        f.write("\n\n")

        # Write the contents of each file
        for file in zip_contents:
            path = os.path.join(extract_to, file)
            if os.path.isfile(path):
                f.write(f"File: {path}\n")
                try:
                    with open(path, "r", encoding="utf-8") as file_content:
                        f.write(file_content.read())
                except UnicodeDecodeError:
                    f.write("[Binary file data not shown]\n")
                f.write("\n\n")


def convert_multiline_to_single_line_and_save(file_path, output_path):
    """
    Converts a multiline text file to a single line text string,
    preserving the newline characters by replacing them with an escaped version.
    This function reads a text file, replaces newline characters with '\\n',
    and saves the single line text to a new file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the file and replace newlines with '\\n'
            single_line_text = file.read().replace('\n', '\\n')

        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(single_line_text)

        return "Conversion and saving successful."
    except Exception as e:
        return str(e)


# Main
zip_path = "my_test.zip"  # Change this to your zip file path
extract_to = "extracted"  # Directory where the zip contents will be extracted
output_file = "output.txt"  # The output file with tree and contents
prologue_file_path = "prologue.txt"  # Path to the prologue file

clear_directory(extract_to)
zip_contents = extract_zip(zip_path, extract_to)
prologue_content = read_prologue_file(prologue_file_path)
write_tree_and_contents(zip_contents, extract_to, output_file, prologue_content)
convert_multiline_to_single_line_and_save(output_file, "output_oneliner.txt")
