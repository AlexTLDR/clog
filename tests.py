from functions.write_file import write_file


def test():
    # Test writing to existing file (lorem.txt)
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for writing to lorem.txt:")
    print(result)
    print("")

    # Test writing to new file in subdirectory (pkg/morelorem.txt)
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for writing to pkg/morelorem.txt:")
    print(result)
    print("")

    # Test trying to write outside working directory - should return error
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for writing to /tmp/temp.txt (should be error):")
    print(result)
    print("")


if __name__ == "__main__":
    test()
