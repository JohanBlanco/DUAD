<aside>
💪🏽 **Ejercicios**

1. Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

```python
with open('unordered playlist.txt') as unordered_playlist:
    lines = unordered_playlist.readlines()
    lines.sort()
    for line in lines:
        with open('ordered playlis.txt', 'a') as ordered_playlist:
            ordered_playlist.write(line)
```

1. Lea sobre el resto de métodos de la clase File de Python [aquí](https://www.w3schools.com/python/python_ref_file.asp) y cree una tabla donde explique qué hace cada uno. **No necesita usar código para esto, es solo crear una tabla en Notion o Word.**
    1. Siga el siguiente formato:

| Método | Descripción |
| --- | --- |
| `read()` | Lee y retorna todo el contenido del archivo |
| `readlines()` | Lee todo el contenido del archivo y retorna una lista con cada línea. |
| `write()` | Escribe contenidos en un archivo. |
| [close()](https://www.w3schools.com/python/ref_file_close.asp) | Closes the file |
| detach() | Returns the separated raw stream from the buffer |
| [fileno()](https://www.w3schools.com/python/ref_file_fileno.asp) | Returns a number that represents the stream, from the operating system's perspective |
| [flush()](https://www.w3schools.com/python/ref_file_flush.asp) | Flushes the internal buffer |
| [isatty()](https://www.w3schools.com/python/ref_file_isatty.asp) | Returns whether the file stream is interactive or not |
| [readable()](https://www.w3schools.com/python/ref_file_readable.asp) | Returns whether the file stream can be read or not |
| [readline()](https://www.w3schools.com/python/ref_file_readline.asp) | Returns one line from the file |
| [seek()](https://www.w3schools.com/python/ref_file_seek.asp) | Change the file position |
| [seekable()](https://www.w3schools.com/python/ref_file_seekable.asp) | Returns whether the file allows us to change the file position |
| [tell()](https://www.w3schools.com/python/ref_file_tell.asp) | Returns the current file position |
| [truncate()](https://www.w3schools.com/python/ref_file_truncate.asp) | Resizes the file to a specified size |
| [writable()](https://www.w3schools.com/python/ref_file_writable.asp) | Returns whether the file can be written to or not |
| [write()](https://www.w3schools.com/python/ref_file_writelines.asp) | Writes a list of strings to the file |
</aside>