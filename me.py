def greet(name):
    """
    Function to greet a user by their name.
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name)) 