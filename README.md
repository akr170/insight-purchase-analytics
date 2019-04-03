# Purchase-Analytics

## Algorithm
Step 1: Read `products.csv` file and store product id and department id in a dictionary as key value pair such that `dictionary[product_id] = department_id`.

Step 2: Read `order_products.csv` file line by line. Determine `department_id` using the `product_id` from each line. Store number of orders and number of reorders in a dictionary such that `dictionary[department_id] = [num_of_orders, num_of_reorders]`

Step 3: Extract all keys from the dictionary using the method `dictionary.keys()`, convert those to a list and sort that list such that the keys are in ascending order.

Step 4: Loop through the sorted dictionary keys and start building the text for output file `report.csv` using the info from dictionary of step 2 and the sorted dictionary keys.


# Questions?
Email us at ashishkumar@umass.edu
