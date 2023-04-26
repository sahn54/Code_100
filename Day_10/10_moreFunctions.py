# functions with outputs

# def my_functions():
#     result = 3 * 2
#     return result


# output = my_functions
# print(output)


def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
# title() changes the string that first letter is cap and other not


print(format_name('SUNG', 'ahn'))
