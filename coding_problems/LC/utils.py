def get_first_key_by_value(dict, value):
    list_of_items = dict.items()
    if value == 0:
        return ""
    else:
        for item in list_of_items:
            if item[1] == value:
                return item[0]