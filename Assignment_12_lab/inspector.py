
"""
Nmae - Sneha Gautam
Roll-no - a26mtai0019
SourceAuditor checks Python source code and package structure.

The property setter validates target_path whenever it is assigned.
An initialization-only check would validate the path just once.
"""

import ast
import os
import re


class SourceAuditor:

    def __init__(self, target_path: str, /) -> None:
        # Assigning through the property automatically calls its setter.
        self.target_path = target_path

    @property
    def target_path(self) -> str:
        # Return the validated path stored inside the object.
        return self._target_path

    @target_path.setter
    def target_path(self, value: str) -> None:
        # Check that the given path exists before storing it.
        if not os.path.exists(value):
            raise FileNotFoundError(
                f"Target path '{value}' does not exist."
            )

        # Store the path only after validation succeeds.
        self._target_path = value

    def audit_module_structure(
        self, file_contents: str, /, *, max_line_length: int = 79
    ) -> dict:
        """Check function spacing and selected style rules."""

        # Convert the source code string into an Abstract Syntax Tree.
        tree = ast.parse(file_contents)

        # Store the names of functions that violate spacing rules.
        spacing_violations = []

        # Select only top-level synchronous and asynchronous functions.
        functions = [
            node for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        ]

        # Compare each function with the function immediately before it.
        for previous, current in zip(functions, functions[1:]):

            # For decorated functions, use the first decorator's line.
            # Otherwise, use the line containing the function definition.
            if current.decorator_list:
                current_start = current.decorator_list[0].lineno
            else:
                current_start = current.lineno

            # Count the blank lines between the two functions.
            blank_lines = current_start - previous.end_lineno - 1

            # PEP 8 requires at least two blank lines between top-level functions.
            if blank_lines < 2:
                spacing_violations.append(current.name)

        # These lists store line numbers for each style violation.
        line_length_violations = []
        trailing_whitespace_violations = []
        colon_spacing_violations = []

        # Examine each source line, keeping its original line number.
        for line_number, line in enumerate(
            file_contents.splitlines(), start=1
        ):

            # Report lines that exceed the permitted maximum length.
            if len(line) > max_line_length:
                line_length_violations.append(line_number)

            # Report trailing whitespace, but ignore blank or whitespace-only lines.
            if line.strip() and line.rstrip() != line:
                trailing_whitespace_violations.append(line_number)

            # Find simple annotation-style colons that have no space after them.
            # Example: phrase:str is flagged, while phrase: str is not.
            if re.search(r"\b[A-Za-z_]\w*:(?=\S)", line):
                colon_spacing_violations.append(line_number)

        # Return all detected violations in a dictionary.
        return {
            "spacing_violations": spacing_violations,
            "line_length_violations": line_length_violations,
            "trailing_whitespace_violations":
                trailing_whitespace_violations,
            "colon_spacing_violations": colon_spacing_violations,
        }

    def verify_sdist_layout(self, directory_path: str, /) -> bool:
        """Validate the required source distribution files."""

        # Create paths for the required setup.py and README.txt files.
        setup_path = os.path.join(directory_path, "setup.py")
        readme_path = os.path.join(directory_path, "README.txt")

        # Both required files must exist.
        if not os.path.isfile(setup_path):
            return False

        if not os.path.isfile(readme_path):
            return False

        # Read and parse setup.py. Return False if it cannot be read or parsed.
        try:
            with open(setup_path, encoding="utf-8") as setup_file:
                setup_tree = ast.parse(setup_file.read())
        except (OSError, SyntaxError, UnicodeError):
            return False

        # Collect module names from literal py_modules lists or tuples.
        module_names = []

        # Walk through the syntax tree to find function calls and their keywords.
        for node in ast.walk(setup_tree):
            if not isinstance(node, ast.Call):
                continue

            for keyword in node.keywords:
                if keyword.arg == "py_modules":

                    # Accept only a literal list or tuple for py_modules.
                    if isinstance(keyword.value, (ast.List, ast.Tuple)):
                        for item in keyword.value.elts:

                            # Keep module names that are literal strings.
                            if isinstance(item, ast.Constant):
                                if isinstance(item.value, str):
                                    module_names.append(item.value)

        # Check whether at least one listed module has a matching .py file.
        for module_name in module_names:
            module_path = os.path.join(
                directory_path, module_name + ".py"
            )

            if os.path.isfile(module_path):
                return True

        # No listed module matched an existing Python file.
        return False


if __name__ == "__main__":

    # Self-test: audit this file and ensure it has no function-spacing violations.
    assert not SourceAuditor(__file__).audit_module_structure(
        open(__file__, encoding="utf-8").read()
    )["spacing_violations"], "Self-audit failed: spacing violations found."

    print("Self-audit passed: no top-level function spacing violations.")

    # Test multiple style rules using a deliberately flawed source sample.
    sample = (
        "def first(phrase:str):\n"
        "    return phrase  \n"
        "def second():\n"
        "    pass\n"
    )

    print(
        SourceAuditor(__file__).audit_module_structure(sample)
    )

    # Edge case 1: exactly one blank line between functions should be flagged.
    one_blank_line = (
        "def alpha():\n"
        "    pass\n"
        "\n"
        "def beta():\n"
        "    pass\n"
    )

    print(
        SourceAuditor(__file__).audit_module_structure(
            one_blank_line
        )["spacing_violations"]
    )

    # Edge case 2: use the decorator's line when checking function spacing.
    decorated_sample = (
        "def alpha():\n"
        "    pass\n"
        "\n"
        "@staticmethod\n"
        "def beta():\n"
        "    pass\n"
    )

    print(
        SourceAuditor(__file__).audit_module_structure(
            decorated_sample
        )["spacing_violations"]
    )

    # Edge case 3: verify that a package missing README.txt is rejected.
    # Keep test_package in the same folder as this inspector.py file.
    test_directory = os.path.join(
        os.path.dirname(__file__), "test_package"
    )

    print(
        SourceAuditor(__file__).verify_sdist_layout(test_directory)
    )

    # Edge case 4: a whitespace-only blank line should not be reported
    # as a trailing-whitespace violation.
    sample = """def alpha():
    pass
    
def beta():
    pass
"""

    print(SourceAuditor(__file__).audit_module_structure(sample))
