def process_fast_search(filename, search_term):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if search_term in line:
                return line