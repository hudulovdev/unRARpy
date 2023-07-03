import rarfile

def extract_rar(file_path, output_dir):
    with rarfile.RarFile(file_path, 'r') as archive:
        archive.extractall(output_dir)

# Example usage:
file_path = 'archive.rar'
output_dir = 'extracted_files'

extract_rar(file_path, output_dir)
