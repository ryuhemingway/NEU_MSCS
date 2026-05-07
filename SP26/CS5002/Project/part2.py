import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# REUSED FROM PART 1 — gradient descent infrastructure
# =============================================================================

def approx_partial_x(f, x, y, h=1e-7):
    # approximates the partial derivative of f with respect to x
    # we will nudge x by a small amount h and hold y constant
    return (f(x + h, y) - f(x, y)) / h


def approx_partial_y(f, x, y, h=1e-7):
    # approximates the partial derivative of f with respect to y
    # we will nudge y by a small amount h and hold x constant
    return (f(x, y + h) - f(x, y)) / h


def gradient_descent_2d(f, x0, y0, alpha, epsilon, iter_max=100000):
    # gradient descent for a two variable function f(x, y)
    # same logic as the 1D version but now we update both x and y each iteration
    # we want to stop when both x and y have converged
    x = x0
    y = y0
    iter = 0
    while iter < iter_max:
        grad_x = approx_partial_x(f, x, y)
        grad_y = approx_partial_y(f, x, y)
        x_new = x - alpha * grad_x
        y_new = y - alpha * grad_y

        # both x and y must converge before we stop
        if abs(x_new - x) < epsilon and abs(y_new - y) < epsilon:
            x = x_new
            y = y_new
            iter += 1
            break
        x = x_new
        y = y_new
        iter += 1
    return x, y, iter


# =============================================================================
# DATA LOADING
# =============================================================================

def load_data(filename):
    '''
    Load the data into two arrays

    Args:
        filename: string representing the name of the file
        containing the data (x,y)

    Return:
        array containing the values of x
        array containing the values of y
    '''
    data = np.loadtxt(filename)
    return data[:, 0], data[:, 1]


# =============================================================================
# COST FUNCTION
# =============================================================================

def cost_function(a, b, x, y):
    '''
    Computes the cost function g(a, b) = sum of (a*x(i) + b - y(i))^2
    for all data points. As specified in the PDF it can take any a,b,x,y values

    This measures how far our linear model f(x) = ax + b is from
    the actual data. We want to minimize this.

    Args:
        a: slope of the linear model
        b: intercept of the linear model
        x: array of x values (cholesterol levels)
        y: array of y values (diastolic blood pressure)

    Return:
        the total squared error (a scalar)
    '''
    n = len(x)
    total = 0.0
    for i in range(n):
        total += (a * x[i] + b - y[i]) ** 2
    return total


# =============================================================================
# SECTION 1 — LINEAR MODEL ON LINEAR DATA
# =============================================================================

def section_1():
    print("=" * 70)
    print("SECTION 1 — COST FUNCTION AND LINEAR MODEL")
    print("=" * 70)
    print()

    # Part 1: load the data
    x, y = load_data('data_chol_dias_pressure.txt')
    print("Part 1: Data loaded successfully.")
    print("Number of patients: " + str(len(x)))
    print("x (cholesterol) range: " + str(round(min(x), 2)) + " to " + str(round(max(x), 2)))
    print("y (diastolic BP) range: " + str(round(min(y), 2)) + " to " + str(round(max(y), 2)))
    print()

    # Part 2: define g(a, b) as a function of two variables for gradient descent
    # we need a wrapper that takes (a, b) so it matches gradient_descent_2d's signature
    def g(a, b):
        return cost_function(a, b, x, y)

    # Part 3: apply gradient descent to find optimal a and b
    # the hint says scaling helps convergence, so we will standardize x and y
    # z-score: x_scaled = (x - mean(x)) / std(x), same for y
    x_mean = np.mean(x)
    x_std = np.std(x)
    y_mean = np.mean(y)
    y_std = np.std(y)

    x_scaled = (x - x_mean) / x_std
    y_scaled = (y - y_mean) / y_std

    print("Part 3: Scaling the data to help gradient descent converge.")
    print("x_mean = " + str(round(x_mean, 4)) + ", x_std = " + str(round(x_std, 4)))
    print("y_mean = " + str(round(y_mean, 4)) + ", y_std = " + str(round(y_std, 4)))
    print()

    # define cost function on scaled data
    def g_scaled(a_s, b_s):
        return cost_function(a_s, b_s, x_scaled, y_scaled)

    # run gradient descent on the scaled data
    # with scaled data, reasonable initial guess is a=0, b=0
    alpha = 0.001
    epsilon = 1e-8
    a_s_opt, b_s_opt, iters = gradient_descent_2d(g_scaled, x0=0, y0=0,
                                                   alpha=alpha, epsilon=epsilon)

    print("Gradient descent on scaled data:")
    print("alpha = " + str(alpha) + ", epsilon = " + str(epsilon))
    print("a_scaled* = " + str(round(a_s_opt, 6)) + ", b_scaled* = " + str(round(b_s_opt, 6)))
    print("Iterations: " + str(iters))
    print()

    # convert back to original scale
    # if y_scaled = a_s * x_scaled + b_s, then
    # (y - y_mean)/y_std = a_s * (x - x_mean)/x_std + b_s
    # y = a_s * (y_std/x_std) * x + (b_s * y_std + y_mean - a_s * y_std * x_mean / x_std)
    a_opt = a_s_opt * (y_std / x_std)
    b_opt = b_s_opt * y_std + y_mean - a_s_opt * y_std * x_mean / x_std

    print("Converting back to original scale:")
    print("a* = " + str(round(a_opt, 6)))
    print("b* = " + str(round(b_opt, 6)))
    print("Linear model: y = " + str(round(a_opt, 4)) + " * x + " + str(round(b_opt, 4)))
    print()

    # compute final cost on original data
    final_cost = cost_function(a_opt, b_opt, x, y)
    print("Final cost g(a*, b*) = " + str(round(final_cost, 4)))
    print()

    # Part 4: plot the line along with data points
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue', label='Patient Data', zorder=5)
    x_line = np.linspace(min(x) - 5, max(x) + 5, 200)
    y_line = a_opt * x_line + b_opt
    plt.plot(x_line, y_line, color='red',
             label='Best Fit: y = ' + str(round(a_opt, 4)) + 'x + ' + str(round(b_opt, 4)))
    plt.xlabel('Total Cholesterol Level (mmol/L)')
    plt.ylabel('Diastolic Blood Pressure (mm Hg)')
    plt.title('Linear Model Fit to Diastolic Blood Pressure Data')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('section1_linear_fit.png', dpi=150)
    plt.show()

    return a_opt, b_opt


# =============================================================================
# SECTION 2 — NON-LINEAR DATA
# =============================================================================

def section_2():
    print("=" * 70)
    print("SECTION 2 — NON-LINEAR DATA")
    print("=" * 70)
    print()

    # Part 1: load the new data
    x, y = load_data('data_chol_dias_pressure_non_lin.txt')
    print("Part 1: Non-linear data loaded successfully.")
    print("Number of patients: " + str(len(x)))
    print("x range: " + str(round(min(x), 2)) + " to " + str(round(max(x), 2)))
    print("y range: " + str(round(min(y), 2)) + " to " + str(round(max(y), 2)))
    print()

    # Part 2: apply gradient descent with linear model on scaled data
    x_mean = np.mean(x)
    x_std = np.std(x)
    y_mean = np.mean(y)
    y_std = np.std(y)

    x_scaled = (x - x_mean) / x_std
    y_scaled = (y - y_mean) / y_std

    def g_scaled_linear(a_s, b_s):
        return cost_function(a_s, b_s, x_scaled, y_scaled)

    alpha = 0.001
    epsilon = 1e-8
    a_s_opt, b_s_opt, iters = gradient_descent_2d(g_scaled_linear, x0=0, y0=0,
                                                   alpha=alpha, epsilon=epsilon)

    # convert back to original scale
    a_opt = a_s_opt * (y_std / x_std)
    b_opt = b_s_opt * y_std + y_mean - a_s_opt * y_std * x_mean / x_std

    print("Part 2: Linear model on non-linear data")
    print("a* = " + str(round(a_opt, 6)) + ", b* = " + str(round(b_opt, 6)))
    print("Iterations: " + str(iters))
    linear_cost = cost_function(a_opt, b_opt, x, y)
    print("Cost g(a*, b*) = " + str(round(linear_cost, 4)))
    print()

    # Part 3: plot the linear fit
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue', label='Patient Data', zorder=5)
    x_line = np.linspace(min(x) - 5, max(x) + 5, 200)
    y_line_linear = a_opt * x_line + b_opt
    plt.plot(x_line, y_line_linear, color='red',
             label='Linear Fit: y = ' + str(round(a_opt, 4)) + 'x + ' + str(round(b_opt, 4)))
    plt.xlabel('Total Cholesterol Level (mmol/L)')
    plt.ylabel('Diastolic Blood Pressure (mm Hg)')
    plt.title('Linear Model Fit to Non-Linear Data')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('section2_linear_fit.png', dpi=150)
    plt.show()

    # Part 4: improve the model — use a quadratic f(x) = ax^2 + bx + c
    print("Part 4: Quadratic model f(x) = a*x^2 + b*x + c")
    print()

    # define the quadratic cost function
    def cost_quadratic(a, b, c, x, y):
        '''
        Cost function for the quadratic model f(x) = ax^2 + bx + c.
        g(a,b,c) = sum of (a*x(i)^2 + b*x(i) + c - y(i))^2

        Args:
            a: coefficient of x^2
            b: coefficient of x
            c: intercept
            x: array of x values
            y: array of y values

        Return:
            the total squared error
        '''
        n = len(x)
        total = 0.0
        for i in range(n):
            total += (a * x[i] ** 2 + b * x[i] + c - y[i]) ** 2
        return total

    # we need gradient descent for 3 variables
    # extending the 2D version from Part 1 to 3D
    def approx_partial(f_3d, a, b, c, var_index, h=1e-7):
        '''
        Approximates the partial derivative of f_3d with respect to the
        variable at var_index (0=a, 1=b, 2=c).

        Args:
            f_3d: function of three variables f(a, b, c)
            a, b, c: current values
            var_index: which variable to differentiate (0, 1, or 2)
            h: small perturbation

        Return:
            approximate partial derivative
        '''
        if var_index == 0:
            return (f_3d(a + h, b, c) - f_3d(a, b, c)) / h
        elif var_index == 1:
            return (f_3d(a, b + h, c) - f_3d(a, b, c)) / h
        else:
            return (f_3d(a, b, c + h) - f_3d(a, b, c)) / h

    def gradient_descent_3d(f_3d, a0, b0, c0, alpha, epsilon, iter_max=100000):
        '''
        Gradient descent for a function of three variables.
        Same logic as gradient_descent_2d but now we update a, b, and c each iteration.

        Args:
            f_3d: function of three variables
            a0, b0, c0: initial guesses
            alpha: learning rate
            epsilon: convergence threshold
            iter_max: maximum iterations

        Return:
            optimal a, b, c and number of iterations
        '''
        a = a0
        b = b0
        c = c0
        iter = 0
        while iter < iter_max:
            grad_a = approx_partial(f_3d, a, b, c, 0)
            grad_b = approx_partial(f_3d, a, b, c, 1)
            grad_c = approx_partial(f_3d, a, b, c, 2)
            a_new = a - alpha * grad_a
            b_new = b - alpha * grad_b
            c_new = c - alpha * grad_c

            # all three must converge
            if (abs(a_new - a) < epsilon and abs(b_new - b) < epsilon
                    and abs(c_new - c) < epsilon):
                a = a_new
                b = b_new
                c = c_new
                iter += 1
                break
            a = a_new
            b = b_new
            c = c_new
            iter += 1
        return a, b, c, iter

    # scale the data for the quadratic model
    # for quadratic, we scale x and y the same way
    def g_quad_scaled(a_s, b_s, c_s):
        return cost_quadratic(a_s, b_s, c_s, x_scaled, y_scaled)

    alpha_q = 0.001
    epsilon_q = 1e-8
    a_s_q, b_s_q, c_s_q, iters_q = gradient_descent_3d(g_quad_scaled,
                                                         a0=0, b0=0, c0=0,
                                                         alpha=alpha_q,
                                                         epsilon=epsilon_q)

    print("Gradient descent on scaled data (quadratic model):")
    print("a_scaled* = " + str(round(a_s_q, 6)))
    print("b_scaled* = " + str(round(b_s_q, 6)))
    print("c_scaled* = " + str(round(c_s_q, 6)))
    print("Iterations: " + str(iters_q))
    print()

    # convert quadratic coefficients back to original scale
    # if y_scaled = a_s * x_scaled^2 + b_s * x_scaled + c_s, then
    # (y - y_mean)/y_std = a_s * ((x - x_mean)/x_std)^2 + b_s * ((x - x_mean)/x_std) + c_s
    # expanding and collecting terms to get y = A*x^2 + B*x + C:
    A = a_s_q * y_std / (x_std ** 2)
    B = b_s_q * y_std / x_std - 2 * a_s_q * y_std * x_mean / (x_std ** 2)
    C = (a_s_q * y_std * x_mean ** 2 / (x_std ** 2)
         - b_s_q * y_std * x_mean / x_std
         + c_s_q * y_std + y_mean)

    print("Converting back to original scale:")
    print("A* = " + str(round(A, 8)))
    print("B* = " + str(round(B, 6)))
    print("C* = " + str(round(C, 4)))
    print("Quadratic model: y = " + str(round(A, 8)) + " * x^2 + "
          + str(round(B, 6)) + " * x + " + str(round(C, 4)))
    print()

    # compute cost for quadratic on original data
    quad_cost = cost_quadratic(A, B, C, x, y)
    print("Quadratic cost = " + str(round(quad_cost, 4)))
    print("Linear cost    = " + str(round(linear_cost, 4)))
    print()

    # plot the quadratic fit alongside the linear fit and the data
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='blue', label='Patient Data', zorder=5)

    x_line = np.linspace(min(x) - 5, max(x) + 5, 200)
    y_line_linear = a_opt * x_line + b_opt
    y_line_quad = A * x_line ** 2 + B * x_line + C

    plt.plot(x_line, y_line_linear, color='red', linestyle='--',
             label='Linear Fit (cost = ' + str(round(linear_cost, 2)) + ')')
    plt.plot(x_line, y_line_quad, color='green',
             label='Quadratic Fit (cost = ' + str(round(quad_cost, 2)) + ')')
    plt.xlabel('Total Cholesterol Level (mmol/L)')
    plt.ylabel('Diastolic Blood Pressure (mm Hg)')
    plt.title('Linear vs Quadratic Model on Non-Linear Data')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('section2_quad_fit.png', dpi=150)
    plt.show()

    return A, B, C


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("PROJECT 1 | PART 2")
    print("Ryu Hemingway")
    print()
    a_opt, b_opt = section_1()
    print()
    A, B, C = section_2()

if __name__ == "__main__":
    main()