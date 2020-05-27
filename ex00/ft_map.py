def ft_map(function_to_apply, list_of_input):
    result = []
    if isinstance(list_of_input, dict):
        for k in list_of_input.keys():
            result.append(function_to_apply(k))
        return result
    else:
        try:
            for i in list_of_input:
                result.append(function_to_apply(i))
            return result
        except NotImplementedError:
            raise NotImplementedError
