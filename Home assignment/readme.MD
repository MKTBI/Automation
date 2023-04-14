
# Jackpot Calculator

## Purpose
The purpose of this Flask app is to offer a user-friendly web interface that enables users to determine the frequency of occurrence of their selected set of EuroJackpot numbers in the lottery draw over a specified number of years, as defined by the user-input value N.

## Dependencies
the app requiers following modual 

1.Flask (for building the web interface)
2.datetime (for date/time related operations)
3.requests (for making HTTP requests)
4.BeautifulSoup (for parsing HTML data)

## App Routes
The app defines two routes:

'/' - This route renders the homepage of the app, which includes a form for user input.
'/calculate' - This route processes the user input from the form, calls the get_numbers_count function, and renders the results on the result page.
get_numbers_count Function
This function takes two arguments:

numbers: a comma-separated string of EuroJackpot numbers to search for.
lookback_years: the number of years to search for the given set of numbers.
The function iterates over each year in the range [current year - lookback_years, current year] and fetches the EuroJackpot draw results for that year from the euro-jackpot.net website. For each draw, the function checks if the given set of numbers is a subset of the draw numbers, and increments the count if so. The function returns a dictionary containing the total count and a list of years in which the given set of numbers appeared.

## App Execution
If the Flask app is executed directly (i.e., __name__ == '__main__'), it runs the app in debug mode.
