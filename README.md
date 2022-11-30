## This is a project that pulls data off starwar API
### Task 2
The task 2 goes like following:
Pull data for the the first movie in star wars
Write the json data into a file named output.txt
#### SUBTASKS -
1. Output should be only list of names (first name & last name) of characters in the
movie.
2. Output should only print list of planet names used in the movie
3. Output should only print list of vehicle names used in the movie.
##### Notes/Warnings
Random number generator may produce some integers IDs within range(1, 82) which
may not yield any results from starwars API (404s). In which case, we skip those IDs
and store the rest.