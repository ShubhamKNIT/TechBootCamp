def list_files(dir, curr_path=''):
    """
    Recursively lists all files in a nested directory structure.
    @params dir: nested dictionary representing the directory structure
    @params curr_path: current path in the recursion
    @returns list of file paths
    """
    files = [] 
    for file in dir.keys():
        if dir[file] is None:
            files.append(f"{curr_path}/{file}")
        else:
            _files = list_files(dir[file], f"{curr_path}/{file}")
            files.extend(_files)
    return files


if __name__ == "__main__":
    directory = {
        "Documents": {
            "Proposal.docx": None,
            "Receipts": {
                "January": {
                    "receipt1.txt": None,
                    "receipt2.txt": None
                },
                "February": {
                    "receipt3.txt": None
                }
            }
        },
    }

    all_files = list_files(directory, '')
    print("Files in Directory:")
    for f in all_files:
        print(f)

