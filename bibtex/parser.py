def get_values_from_data(data, identifier_name):
    ret = []
    for item in data:
        val = ''
        for k, v in item.items():
            if k == identifier_name:
                val = str(v) + ',\n' + val
                continue
            val += k + ' = \t' + str(v) + ',\n'
        ret.append(val)
    return ret


def parser(data, data_type, identifier_name='id'):
    ret = get_values_from_data(data, identifier_name)
    result = ''
    for item in ret:
        result += '@' + data_type + '{' + item + '}\n'
    return result


def parser_by_field(data, data_type_in_dict='entry_type', identifier_name='id'):
    ret = get_values_from_data(data, identifier_name)
    result = ''
    for item in ret:
        result += '@' + data[data_type_in_dict] + '{' + item + '}\n'
    return result
