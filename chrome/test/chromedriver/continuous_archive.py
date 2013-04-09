# Copyright (c) 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Downloads items from the Chromium continuous archive."""

import os
import sys
import urllib

_THIS_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(_THIS_DIR, os.pardir, 'pylib'))

from common import util

CHROME_26_REVISION = '181664'
CHROME_27_REVISION = '190466'

_SITE = 'http://commondatastorage.googleapis.com/chromium-browser-continuous'


def GetLatestRevision():
  """Returns the latest revision (as a string) available for this platform."""
  url = _SITE + '/%s/LAST_CHANGE'
  return urllib.urlopen(url % _GetDownloadPlatform()).read()


def DownloadChrome(revision, dest_dir):
  """Downloads the packaged Chrome from the archive to the given directory.

  Args:
    revision: the revision of Chrome to download.
    dest_dir: the directory to download Chrome to.

  Returns:
    The path to the unzipped Chrome binary.
  """
  def GetZipName():
    if util.IsWindows():
      return 'chrome-win32'
    elif util.IsMac():
      return 'chrome-mac'
    elif util.IsLinux():
      return 'chrome-linux'
  def GetChromePathFromPackage():
    if util.IsWindows():
      return 'chrome.exe'
    elif util.IsMac():
      return 'Chromium.app/Contents/MacOS/Chromium'
    elif util.IsLinux():
      return 'chrome'
  zip_path = os.path.join(dest_dir, 'chrome-%s.zip' % revision)
  if not os.path.exists(zip_path):
    url = _SITE + '/%s/%s/%s.zip' % (_GetDownloadPlatform(), revision,
                                     GetZipName())
    print 'Downloading', url, '...'
    urllib.urlretrieve(url, zip_path)
  util.Unzip(zip_path, dest_dir)
  return os.path.join(dest_dir, GetZipName(), GetChromePathFromPackage())


def _GetDownloadPlatform():
  """Returns the name for this platform on the archive site."""
  if util.IsWindows():
    return 'Win'
  elif util.IsMac():
    return 'Mac'
  elif util.IsLinux():
    return 'Linux_x64'
