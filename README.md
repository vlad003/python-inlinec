# Inline C in Python

Well, not really inline. You write it in a string.

Here's an example:

    import inlinec
    import timeit

    def f1(x):
        y = 5
        for i in range(x):
            y = y*i % x

        return y

    f2 = inlinec.gcc("""int f(int x) {
                            int y = 5;
                            for (int i = 0; i < x; i++) {
                                y = y*i % x;
                            }
                            return y;
                        }""")

    print("Computing in Python")
    print(timeit.timeit("f1(256)", globals=globals()))
    print("Computing in C")
    print(timeit.timeit("f2(256)", globals=globals()))

On my machine, I get the following output:

    Computing in Python
    21.455355852958746
    Computing in C
    2.906890120008029

Of course, the benefits really depend on your functions and how often you run
them. The compilation overhead might be too much (although the result is cached)
so you might actually see a slowdown. YMMV.

Although for larger pieces of code, you'll want to go the old fashioned way and
write your C code in a separate file and compile it yourself, I thought this
would be cool for short things where it'd be nice to see the function
implementation in your Python source.
