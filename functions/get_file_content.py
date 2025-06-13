import os


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        MAX_CHARS = 10000

        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            # Try to read one more character to see if file is longer
            next_char = f.read(1)

        # If we could read another character, file was truncated
        if next_char:
            file_content_string += f'\n[...File "{file_path}" truncated at 10000 characters]'

        return file_content_string
    except Exception as e:
        return f"Error: {e}"
