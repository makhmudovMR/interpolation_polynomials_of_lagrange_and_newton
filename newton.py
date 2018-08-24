

def div_diff_function(known_points):

    f_cache = {(xi,): yi for xi, yi in sorted(known_points)}

    def f(xs):

        xi_tuple = tuple(sorted(xs))
        if xi_tuple not in f_cache:
            f_cache[xi_tuple] = (f(xi_tuple[1:]) - f(xi_tuple[:-1])) / \
                                float(xi_tuple[-1] - xi_tuple[0])
        return f_cache[xi_tuple]

    return f


def interpolation_polynomial(known_points, get_string=False):

    x_knots = sorted(point[0] for point in known_points)
    n = len(x_knots) - 1
    div_diffs = div_diff_function(known_points)


    coeffs = [div_diffs(x_knots[:i + 1]) for i in range(len(x_knots))]


    def p(x):

        total = coeffs[0]  # coeffs[0] = div_diff(x0) = y0
        basis = 1
        for i in range(n):
            basis = basis * (x - x_knots[i])
            total = total + coeffs[i + 1] * basis
        return total

    return (p, _str_newton_poly(coeffs, x_knots)) if get_string else p


def _str_newton_poly(coeffs, x_knots):

    basis, poly_string = '', str(coeffs[0])
    for ci, xi in zip(coeffs[1:], x_knots[:-1]):
        if xi < 0:
            basis += '(x + ' + str(-xi) + ')'
        elif xi == 0:
            basis += 'x'
        else:
            basis += '(x - ' + str(xi) + ')'


        add = ' + ' if ci >= 0 else ' - '
        if ci == 0:
            next
        elif abs(ci) == 1:
            poly_string += add + basis
        else:
            poly_string += add + str(abs(ci)) + basis
    return 'p(x) = ' + poly_string