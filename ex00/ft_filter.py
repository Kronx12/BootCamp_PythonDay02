def ft_filter(function_to_apply, list_of_inputs):
    res = []
    if isinstance(list_of_inputs, dict):
        for i in list(list_of_inputs.keys()):
            if (function_to_apply(i)):
                res.append(i)
        return res
    else:
        try:
            for i in list(list_of_inputs):
                if (function_to_apply(i)):
                    res.append(i)
            return res
        except NotImplementedError:
            raise NotImplementedError
