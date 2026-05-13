# ============================================================
# Pattern Drill A: BYU Campus Dining
# ============================================================
# The data is already loaded — your job is to write the loops.
# Complete each TODO using a for loop.
# ============================================================

# --- DATA (do not modify) -----------------------------------
restaurants = ["Cupbop", "Costa Vida", "Chick-fil-A", "Subway",
               "Taco Bell", "MOD Pizza", "Panda Express"]
ratings     = [4.5, 4.2, 4.8, 3.1, 3.6, 4.0, 3.9]
prices      = [11.50, 9.75, 8.99, 7.25, 6.99, 10.50, 8.75]
# ------------------------------------------------------------


# TODO 1 — Accumulator
# Calculate the average rating across all restaurants.
total_ratings = 0 
for rating in ratings:
    total_ratings += rating
average_rating = total_ratings/ len(ratings)
# Hint: sum all ratings, then divide by the count.



print(f"Average rating: {average_rating:.2f}")  # replace ___ with your variable


# TODO 2 — Filter
# Build a list of restaurants rated 4.0 or higher.
top_rated_restaurants = []

for i in range(len(ratings)):
    if ratings[i] >= 4.0:
        top_rated_restaurants.append(restaurants[i])
# Hint: loop through the indices so you can check ratings[i]
#       and grab restaurants[i].



print(f"Top-rated (4.0+): {top_rated_restaurants}")  # replace ___ with your list


# TODO 3 — Search
# Check whether "Cupbop" is in the restaurant list.
target = "Cupbop"
found = False
while found == False:
    for restaurant in restaurants:
        if restaurant == target:
            found = True

# Use a boolean flag — do NOT use the `in` operator.
# Hint: start with found = False, flip it inside the loop.



print(f"Cupbop found: {found}")  # replace ___ with your flag


# TODO 4 — Challenge (combine two patterns)
# Which restaurant has the best rating-to-price ratio?
best_value_restaurant = ""
best_value = 0
for i in range(len(restaurants)):
    value_score = ratings[i] / prices[i]
    if value_score > best_value:
        best_rating_restaurant = restaurants[i]
        best_value = value_score
# (rating / price = value score)
# Hint: you need a loop that tracks the best ratio AND
#       which restaurant it belongs to.



print(f"Best value: {best_rating_restaurant} at {best_value:.2f} value score.")  # replace ___ with the restaurant name