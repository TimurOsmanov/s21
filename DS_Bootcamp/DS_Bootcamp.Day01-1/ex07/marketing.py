import sys

def data_init(task: str) -> list:
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill\_gates@live.com', 'mark@facebook.com',
               'elon@paypal.com', 'jessica@gmail.com']
    #  clients’ email accounts
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    # the email accounts of the participants in your most recent event
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    # the accounts of your clients who viewed your most recent promotional email

    call_center: set = (set(clients) | set(participants)) - set(recipients)
    # Create a list of those who have not seen your promotional email yet (operand "-" has primary priority)
    potential_clients: set = set(participants) - set(clients)
    # Create a list of the participants who are not your clients.
    loyalty_program: set = set(clients) - set(participants)
    # Create a list of the clients who did not participate in the event.

    pos: dict = {"call_center": list(call_center),
                 "potential_clients": list(potential_clients),
                 "loyalty_program": list(loyalty_program)}

    return pos[task]


def argv_check(my_argv: list, task_names: list) -> str:
    if len(my_argv) != 2:
        # if there are no arguments or too many arguments, the program displays nothing
        return ""

    if my_argv[1] not in task_names:
        # if there is wrong name
        return ""

    return my_argv[1]


def main() -> None:
    try:
        possible_task_names: list = ["call_center", "potential_clients", "loyalty_program"]
        task_name_checked: str = argv_check(sys.argv, possible_task_names)
        possible_task_names.index(task_name_checked)
        # to raise error if something went wrong
        print(', '.join(data_init(task_name_checked)))

    except ValueError as error:
        print(f"ValueError: {error} - wrong task name or more than one task")


if __name__ == '__main__':
    main()
