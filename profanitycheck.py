from better_profanity import profanity


if __name__ == "__main__": #_ is bascially the top-level script evironment, and it specifies the ierpreter that (I have thhe highest priority to be executed first

    #declared a variable and initialized it, declared an input function
    text = input("Enter a word: ")

    #created a variable, initialized it, to a method adn passed text as the parameter
    censored_text = profanity.censor(text)
    print(censored_text)
    # You **** of ****.
#end of the code