def helper(key, dic, results):
    for k, v in dic.items():
        # print(k,v)
        if type(v) == str:
            if key == "":
                results[k] = v
            else:
                if k == "":
                    results[key] = v
                else:
                    results[key + "." + k] = v
        else:
            if key == "":
                helper(k, v, results)
            else:
                helper(key + "." + k, v, results)


def flatten_dictionary(dictionary):
    results = {}
    helper("", dictionary, results)

    return results


dict = {
    "Key1": "1",
    "Key2": {
        "a": "2",
        "b": "3",
        "c": {
            "d": "3",
            "e": {
                "": "1"
            }
        }
    }
}

flatten_dictionary(dict)