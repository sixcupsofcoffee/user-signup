#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


# TODO 1: Create form with all fields

# TODO 2: Create handler for successful form

# TODO 3: Create error handler

# TODO 4: Add regex to validate

# TODO 5: Connect validation to error handling

# TODO 6: Create correct styling for errors

# TODO 7: Refactor code

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)