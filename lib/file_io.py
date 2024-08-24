def write_file(file_name="lib/test_file", file_content="This is a test content."):
    with open(f'{file_name}.txt', mode="w", encoding="utf-8") as test_file:
        test_file.write(file_content)

def append_file(file_name="lib/test_file", append_content="This is a test content."):
    with open(f'{file_name}.txt', mode="a", encoding="utf-8") as test_file:
        test_file.write(append_content)

def read_file(file_name='test_file'):
    return open(f'{file_name}.txt', encoding='utf-8').read()
