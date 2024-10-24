"""
Module Name: color_print
Author: Haripo Wesley T.
Email: haripowesleyt@gmail.com
GitHub: https://github.com/haripowesleyt
Date Created: 2024-10-24
Version: 1.0
Description: A module to print colored and formatted text using ANSI escape codes.

Implements Python's built-in print() function (see 
https://docs.python.org/3/library/functions.html#print) along with ANSI escape 
sequences to display colored and/or formatted text.

ANSI refers to the American National Standards Institute, and ANSI escape codes are 
sequences of characters used to control text formatting in terminals. These codes 
enable changes to text color, background color, and other display attributes. This 
module utilizes ANSI escape sequences to print text with specified colors (foreground 
and/or background) and formats (e.g., bold, italic, underlined).
"""


def cprint(
    *objects,
    fg: str = "",
    bg: str = "",
    fmt: str = "",
    sep: str = " ",
    end: str = "\n",
    file: object = None,
    flush: bool = False,
) -> None:
    """
    cprint() stands for "color print" and mimics Python's built-in print() function while
    adding display properties like color and format.

    The cprint() function has all the parameters of print() plus three additional
    parameters: fg, bg, and fmt. While these parameters do not alter the internal
    functioning of print(), they enable enhanced display properties. Any valid print()
    statement is also a valid cprint() statement, allowing you to utilize cprint() with the
    added advantage of foreground color, background color, and display formats.

        Supported colors (for both foreground and background) are:
        - black
        - gray / grey
        - red / light-red
        - green / light-green
        - yellow / light-yellow
        - blue / light-blue
        - magenta / light-magenta
        - cyan / light-cyan
        - white / whitesmoke

        Supported formats are:
        - bold: thickens the text
        - dim: reduces the text's transparency
        - italic: leans the text at an angle
        - underline: adds a line beneath the text
        - blink: alternates visibility of the text
        - reverse: swaps the foreground and background colors
        - hidden: makes the text invisible
        - strikethrough: adds a horizontal line through the text

    Note that *objects, sep, end, file, and flush are not cprint()-specific parameters;
    they are borrowed from the built-in print() function. For more information on their
    usage, visit the official documentation at
    https://docs.python.org/3/library/functions.html#print. You can use cprint() just like
    print().

    Args:
        fg (str, optional): Foreground color name (e.g., "red"). Defaults to "".
        bg (str, optional): Background color name (e.g., "green"). Defaults to "".
        fmt (str, optional): Format name (e.g., "strikethrough"). Defaults to "".
        sep (str, optional): Separator between unpacked objects. Defaults to " ".
        end (str, optional): Printed at the end of the line. Defaults to "\n".
        file (object, optional): File to print to instead of the terminal. Defaults to None.
        flush (bool, optional): Whether to forcibly flush the buffered output. Defaults to False.

    Raises:
        ValueError: If an unsupported foreground color name is passed as fg.
        ValueError: If an unsupported background color name is passed as bg.
        ValueError: If an unsupported format name is passed as fmt.
    """

    fg_colors_map: dict = {
        "black": "\033[30m",
        "gray": "\033[90m",
        "grey": "\033[90m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "whitesmoke": "\033[97m",
        "light-red": "\033[91m",
        "light-green": "\033[92m",
        "light-yellow": "\033[93m",
        "light-blue": "\033[94m",
        "light-magenta": "\033[95m",
        "light-cyan": "\033[96m",
    }

    bg_colors_map: dict = {
        "black": "\033[40m",
        "red": "\033[41m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "blue": "\033[44m",
        "magenta": "\033[45m",
        "cyan": "\033[46m",
        "white": "\033[47m",
        "whitesmoke": "\033[107m",
        "gray": "\033[100m",
        "grey": "\033[100m",
        "light-red": "\033[101m",
        "light-green": "\033[102m",
        "light-yellow": "\033[103m",
        "light-blue": "\033[104m",
        "light-magenta": "\033[105m",
        "light-cyan": "\033[106m",
    }

    formats_map: dict = {
        "bold": "\033[1m",
        "dim": "\033[2m",
        "italic": "\033[3m",
        "underline": "\033[4m",
        "blink": "\033[5m",
        "reverse": "\033[7m",
        "hidden": "\033[8m",
        "strikethrough": "\033[9m",
    }

    if fg == "":  # Default value
        fg_ansi_code: str = ""
    else:
        fg_ansi_code: object = fg_colors_map.get(fg)
        if not fg_ansi_code:
            raise ValueError(f"fprint() Error: unrecognised foreground color '{fg}'.")

    if bg == "":  # Default Value
        bg_ansi_code: str = ""
    else:
        bg_ansi_code: object = bg_colors_map.get(bg)
        if not bg_ansi_code:
            raise ValueError(f"fprint() Error: unrecognised background color '{bg}'.")

    if fmt == "":  # Default Value
        fmt_ansi_code: str = ""
    else:
        fmt_ansi_code: object = formats_map.get(fmt)
        if not fmt_ansi_code:
            raise ValueError(f"fprint() Error: unrecognised format style '{fmt}'.")

    ansi_code_for_reset: str = "\033[0m"

    print(fmt_ansi_code, bg_ansi_code, fg_ansi_code, sep="", end="")
    print(
        *objects,
        sep=sep,
        end="",
        file=file,
        flush=flush,
    )
    print(ansi_code_for_reset, end=end)
