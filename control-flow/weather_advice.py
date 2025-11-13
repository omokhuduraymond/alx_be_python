weather = ["sunny","rainy","cold"]
weather_input = input("What's the weather like today? (sunny/rainy/cold): ").lower()
if weather_input == weather[0]:
    print("Wear a t-shirt and sunglasses.")
elif weather_input == weather[1]:
    print("Don't forget your umbrella and a raincoat.")
elif weather_input == weather[2]:
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather")