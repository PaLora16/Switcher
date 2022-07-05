from typing import Callable

"""
Decoratos has 2 levels
    - switcher which decorates main function
    - register applied on "case" functions which save 
    logic determining function calling
"""


def switcher(main: Callable) -> Callable:
    # list for each registered function together with logic
    calls = []

    def register(logic: Callable) -> Callable:
        def _register(spec: Callable) -> Callable:
            calls.append((logic, spec))
            return spec

        return _register

    # calling main function decorated witch @switcher
    def _switcher(*args, **kwargs) -> Callable:
        for call in calls:
            try:

                # core switcher logic: if registered "case" logic
                # evaluate to True,
                if call[0](*args, **kwargs):
                    # then run registered "case" function
                    call[1]()

            # for simplicity we suppress silently any exceptions as no
            # supplied argument etc
            except:
                pass

        # after exhausting  "switch" statement
        # continue with logic in the main function
        main(*args, **kwargs)

    # enable register decorator acces to register
    # logic we must create a new attribute
    _switcher.register = register

    return _switcher
