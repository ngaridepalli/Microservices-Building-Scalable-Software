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
#

from __future__ import print_function

import sys

from twitter.common import app


@app.command(name='help')
def help_command(args, options):
  """Get help about a specific command.
  """
  if len(args) == 0:
    app.help()
  for (command, doc) in app.get_commands_and_docstrings():
    if args[0] == command:
      print('command %s:' % command)
      print(doc)
      app.quit(0)
  print('unknown command: %s' % args[0], file=sys.stderr)
