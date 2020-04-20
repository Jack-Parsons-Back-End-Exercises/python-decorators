def sortByName(returnFunc):
    def newReturn(*args, **kwargs):
        originalReturn = returnFunc(*args, **kwargs)
        return f"""{originalReturn}
            ORDER BY last_name ASC, first_name ASC"""
    return newReturn