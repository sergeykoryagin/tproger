def extension(filename):
    filename_parts = filename.split('.')
    error = False
    if len(filename_parts) < 2:
        error = True
    first, *middle, last = filename_parts
    if not last or not first and not middle:
        error = True
    if error:
        raise ValueError('the file has no extension')
    else:
        return filename_parts[-1]


print(extension('task12.py'))
