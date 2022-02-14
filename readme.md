# Writing tests in Python

## How to structure your tests
You’ll find that, as you add more and more tests, your single file will become cluttered and hard to maintain, so you can create a folder called `tests/` and split the tests into multiple files. It is convention to ensure each file starts with `test_` so all test runners will assume that Python file contains tests to be executed.

## Assertions
There are some general best practices around how to write assertions:
- Make sure tests are repeatable and run your test multiple times to make sure it gives the same result every time
- Try and assert results that relate to your input data, such as checking that the result is the actual sum of values in the `sum()` example

`unittest` comes with lots of methods to assert on the values, types, and existence of variables. Here are some of the most commonly used methods:
- `.assertEqual(a, b)`
- `.assertTrue(x)`
- `.assertFalse(x)`
- `.assertIs(a, b)`
- `.assertIsNone(x)`
- `.assertIn(a, b)`
- `.assertIsInstance(a, b)`

`.assertIs()`, `.assertIsNone()`, `.assertIn()`, and `.assertIsInstance()` all have opposite methods, named `.assertIsNot()`, and so forth.


## Execute the tests
In the command line terminal, at the root project folder `python-tests-project`,
- run the following command: `python test.py`, or
- use the `unittest` command line: `python -m unittest test`.
This will execute the same test module (called `test`) via the command line.

You will see the following output in the terminal window:
```
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK
```

You can provide additional options to change the output. One of those is `-v` for verbose: `python -m unittest -v test` 

You will see the following output in the terminal window:
```
    test_list_int (test.TestSum)
    Test that the function can return a sum of a list of integers. ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 0.001s

    OK
```

Instead of providing the name of a module containing tests, you can request an auto-discovery: `python -m unittest discover`. This will search the current directory for any files named `test*.py` and attempt to test them.

Once you have multiple test files, as long as you follow the `test*.py` naming pattern, you can provide the name of the directory instead by using the `-s` flag and the name of the directory (e.g., a folder called `tests`): `python -m unittest discover -s tests`

Lastly, if your source code is not in the directory root and contained in a subdirectory, for example in a folder called `src/`, you can tell unittest where to execute the tests so that it can import the modules correctly with the `-t` flag: `python -m unittest discover -s tests -t src`. `unittest` will change to the `src/` directory, scan for all `test*.py` files inside the the tests directory, and execute them.

## More advanced testing scenarios

### Fixtures
The data that you create as an input is known as a **fixture**. It’s common practice to create fixtures and reuse them.

### Parameterization
If you’re running the same test and passing different values each time and expecting the same result, this is known as **parameterization**.

### Error handling
You can use `.assertRaises()` as a context-manager, then inside the `with` block execute the test steps.

## Integration tests
