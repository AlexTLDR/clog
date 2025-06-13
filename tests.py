from functions.get_file_content import get_file_content


def test():
    # Test reading lorem.txt - should be truncated at 10000 characters
    result = get_file_content("calculator", "lorem.txt")
    print("Result for lorem.txt (should be truncated):")
    print(f"Length: {len(result)} characters")
    if "truncated at 10000 characters" in result:
        print("✓ File was properly truncated")
    else:
        print("✗ File was not truncated as expected")
    print("")

    # Test reading main.py
    result = get_file_content("calculator", "main.py")
    print("Result for main.py:")
    print(result)
    print("")

    # Test reading pkg/calculator.py
    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for pkg/calculator.py:")
    print(result)
    print("")

    # Test trying to read outside working directory - should return error
    result = get_file_content("calculator", "/bin/cat")
    print("Result for /bin/cat (should be error):")
    print(result)
    print("")


if __name__ == "__main__":
    test()
