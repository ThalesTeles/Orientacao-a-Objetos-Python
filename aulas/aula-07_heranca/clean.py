import io
import tokenize

def remove_comments_and_docstrings(source_code: str) -> str:
    """Removes all single-line comments and triple-quoted docstrings."""
    io_obj = io.StringIO(source_code)
    out = []
    prev_toktype = tokenize.INDENT
    last_lineno = -1
    last_col = 0

    for tok in tokenize.generate_tokens(io_obj.readline):
        token_type = tok.type
        token_string = tok.string
        start_line, start_col = tok.start
        end_line, end_col = tok.end

        # Handle structural line spacing
        if start_line > last_lineno:
            last_col = 0
        if start_col > last_col:
            out.append(" " * (start_col - last_col))

        # 1. Skip # single line comments
        if token_type == tokenize.COMMENT:
            pass

        # 2. Skip multiline/docstrings (strings that appear right after indent/newlines)
        elif token_type == tokenize.STRING:
            if prev_toktype in (tokenize.INDENT, tokenize.NEWLINE, tokenize.NL):
                # Check if it starts with triple quotes
                if token_string.startswith(('"""', "'''")):
                    pass
                else:
                    out.append(token_string)
            else:
                out.append(token_string)
        else:
            out.append(token_string)

        prev_toktype = token_type
        last_lineno = end_line
        last_col = end_col

    return "".join(out)

# --- Example Usage ---
raw_code = """
\"\"\"
Module-level docstring that needs to be removed.
\"\"\"
# A regular line comment
def calculate_total(price, tax):
    \"\"\"Calculates total price with tax (should be removed).\"\"\"
    print("This standard string 'with quotes' stays intact!")  # Inline comment
    return price + tax
"""

cleaned_code = remove_comments_and_docstrings(raw_code)
print(cleaned_code)
