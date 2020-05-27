def ft_reduce(function_to_apply, list_of_inputs):
    if isinstance(list_of_inputs, dict):
        res = list(list_of_inputs.keys())[0]
        for i in list(list_of_inputs.keys())[1:]:
            res = function_to_apply(res, i)
        return res
    else:
        try:
            list_of_inputs = list(list_of_inputs)
            res = list_of_inputs[0]
            for i in list_of_inputs[1:]:
                res = function_to_apply(res, i)
            return res
        except NotImplementedError:
            raise NotImplementedError
