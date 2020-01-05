# template config file for local testing of ttfs with fontbakery.

from fontbakery.checkrunner import Section, PASS, FAIL, WARN, ERROR, INFO, SKIP
from fontbakery.callable import condition, check, disable
from fontbakery.constants import PriorityLevel
from fontbakery.message import Message
from fontbakery.fonts_profile import profile_factory
import re


# imports are used to mix in other external profiles
profile_imports =('fontbakery.profiles.opentype','fontbakery.profiles.name', 'fontbakery.profiles.head', 'fontbakery.profiles.glyf')

# example of import params for SIL common profile and ABS profile directly in pysilfont
# profile_imports = ['silfont.fbtests.common', 'silfont.fbtests.abs']

profile = profile_factory(default_section=Section("SIL font project"))

# Our own checks below
# See https://font-bakery.readthedocs.io/en/latest/developer/writing-profiles.html

# putting this at the top of the file
# can give a quick overview:
expected_check_ids = (
    'org.sil.software/checks/helloworld',
)

# We use `check` as a decorator to wrap an ordinary python
# function into an instance of FontBakeryCheck to prepare
# and mark it as a check.
# A check id is mandatory and must be globally and timely
# unique. See "Naming Things: check-ids" below.
@check(id='org.sil.software/checks/helloworld')
# This check will run only once as it has no iterable
# arguments. Since it has no arguments at all and because
# checks should be idempotent (and this one is), there's
# not much sense in having it all. It will run once
# and always yield the same result.
def hello_world():
  """Simple "Hello (alphabets of the) World" example."""
  # The function name of a check is not very important
  # to create it, only to import it from another module
  # or to call it directly, However, a short line of
  # human readable description is mandatory, preferable
  # via the docstring of the check.

  # A status of a check can be `return`ed or `yield`ed
  # depending on the nature of the check, `return`
  # can only return just one status while `yield`
  # makes a generator out of it and it can produce
  # many statuses.
  # A status also always must be a tuple of (Status, Message)
  # For `Message` a string is OK, but for unit testing
  # it turned out that an instance of `fontbakery.message.Message`
  # can be very useful. It can additionally provide
  # a status code, better suited to figure out the exact
  # check result.
  yield PASS, 'Hello (alphabets of the) World'

# skip checks (they still appear)
def check_skip_filter(checkid, font=None, **iterargs):
  if checkid in (
        'com.google.fonts/check/metadata/reserved_font_name'
      , 'com.google.fonts/check/description/broken_links'
      , 'com.google.fonts/check/name/rfn'
  ):
    return False, ('We do not want or care about these checks')
  return True, None

profile.check_skip_filter = check_skip_filter

# disable checks
def check_disable_filter(checkid, font=None, **iterargs):
  if checkid in (
        'com.google.fonts/check/metadata/reserved_font_name'
      , 'com.google.fonts/check/description/broken_links'
      , 'com.google.fonts/check/name/rfn'
  ):
    return False, ('We do not want or care about these checks')
  return True, None

profile.check_skip_filter = check_skip_filter
profile.check_disable_filter = check_disable_filter
profile.auto_register(globals())
