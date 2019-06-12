def calculator(a: int, b: int, operation: str) -> int or str:
    _dunder_method = {'+': '__add__',
                      '-': '__sub__',
                      '*': '__mul__',
                      '/': '__truediv__',
                      '**': '__pow__'}.get(operation)

    return getattr(a, _dunder_method)(b) if _dunder_method is not None else 'Данная операция не поддерживается!'
