# Copyright 2018 Adrien Guinet <adrien@guinet.me>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# RUN: "%python" "%s"
#

import pydffi
import sys

F = pydffi.FFI()
CU = F.cdef('''
#include <stdint.h>
typedef int32_t MyInt;
typedef struct {
  int a;
  int b;
} A;
''')

assert(CU.types.MyInt == F.Int32Ty)
assert(isinstance(CU.types.A, pydffi.StructType))
