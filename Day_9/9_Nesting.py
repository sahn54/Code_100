# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",

}

# Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting a Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visited": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visited": 5}
}

# Nesting Dictionary in a List
travel_log = [
    {"country": "France",
     "cities_visited": [
         "Paris", "Lille", "Dijon"],
     "total_visited": 12},
    {"country": "Germany",
     "cities_visited": [
         "Berlin", "Hamburg", "Stuttgart"],
     "total_visited": 5}
]
