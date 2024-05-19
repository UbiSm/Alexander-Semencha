def first_vacant_row(seats):

    max_count = 0
    max_row = 0
    for row_index, row in enumerate(seats, 1):  
        available_seats_count = row.count(0)  
        if available_seats_count > max_count:  
            max_row = row_index
            max_count = available_seats_count

    return max_row if max_count > 0 else 0, max_count  
