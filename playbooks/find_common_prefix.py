import sys
import os

def common_prefix(paths):
    if not paths:
        return ""
    
    # Convert paths to lists of directories
    split_paths = [path.split(os.sep) for path in paths]
    
    # Find the common prefix
    prefix = os.sep
    for directories in zip(*split_paths):
        if len(set(directories)) == 1:
            prefix = os.path.join(prefix, directories[0])
        else:
            break

    return prefix

if __name__ == "__main__":
    paths = sys.argv[1:]
    prefix = common_prefix(paths)
    print(prefix)