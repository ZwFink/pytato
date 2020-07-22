__copyright__ = """
Copyright (C) 2020 Andreas Kloeckner
Copyright (C) 2020 Matt Wala
Copyright (C) 2020 Xiaoyu Wei
"""

__license__ = """
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from pytato.array import (
        Namespace, Array, DictOfNamedArrays, Tag, UniqueTag,
        DottedName,

        make_dict_of_named_arrays,
        make_placeholder, make_size_param, make_data_wrapper,

        matmul, roll, transpose, stack,
        )

from pytato.codegen import generate_loopy
from pytato.target import Target, PyOpenCLTarget

__all__ = (
        "DottedName", "Namespace", "Array", "DictOfNamedArrays",
        "Tag", "UniqueTag",

        "make_dict_of_named_arrays", "make_placeholder", "make_size_param",
        "make_data_wrapper",

        "matmul", "roll", "transpose", "stack",

        "generate_loopy",

        "Target", "PyOpenCLTarget",
)
