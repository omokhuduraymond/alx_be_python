weather = ["sunny","rainy","cold"]
enter = input("What is the weather like today(sunny/rainy/cold: ").lower()
if enter == weather[0]:
    print("Wear a t-shirt and sunglasses.")
elif enter == weather[1]:
    print("Don't forget your umbrella and a raincoat.")
elif enter == weather[2]:
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather")