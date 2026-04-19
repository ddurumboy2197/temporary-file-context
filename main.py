import tempfile

with tempfile.TemporaryFile() as f:
    f.write(b"Hello, world!")
