"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    letters = 'ABCD'
    for i in range(number):
        yield letters[i % len(letters)]

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    letters = 'ABCD'
    generated_seats = 0
    row = 1
    while generated_seats< number:
        if row == 13:
            row += 1
            continue
        for seat in letters:
            if generated_seats >= number:
                break
            yield f"{row}{seat}"
            generated_seats += 1
        row += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    number_of_people = len(passengers)
    generated_seats = generate_seats(number_of_people)
    assign_seats = {}
    for index , seat in enumerate(generated_seats):
        assign_seats[passengers[index]] = assign_seats.get(passengers[index],seat)
    return assign_seats

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        code = seat + flight_id
        if len(code) < 12:
            code = code + '0' * (12 - len(code))
        yield code