while True:
    try:
        number = int(input("What is your fav number hoss?\n"))
        print(1/number)
        break
    except ValueError:
        print("Make sure the typo")
    except ZeroDivisionError:
        print("Don't pick zero hoss!")
    #no matter what other problems, this will break. But not recommended!
    except:
        break
    finally: #No matter what it will show.
        print("Loop complete!")

