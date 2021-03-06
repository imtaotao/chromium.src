// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "nacl_io/path.h"

#include <stdio.h>
#include <string.h>
#include <string>

#include "sdk_util/string_util.h"

namespace nacl_io {

Path::Path(const Path& path) {
  paths_ = path.paths_;
}

Path::Path(const std::string& path) {
  Set(path);
}

bool Path::IsAbsolute() const {
  return !paths_.empty() && paths_[0] == "/";
}

const std::string& Path::Part(size_t index) const {
  return paths_[index];
}

size_t Path::Size() const {
  return paths_.size();
}

bool Path::IsRoot() const {
  return paths_.empty() || (paths_.size() == 1 && paths_[0] == "/");
}

Path& Path::MakeRelative() {
  if (IsAbsolute()) {
    paths_.erase(paths_.begin());
  }
  return *this;
}

Path& Path::Append(const Path& path) {
  // Appending an absolute path effectivly sets the path, ignoring
  // the current contents.
  if (path.IsAbsolute()) {
    paths_ = path.paths_;
  } else {
    for (size_t index = 0; index < path.paths_.size(); index++) {
      paths_.push_back(path.paths_[index]);
    }
  }

  paths_ = Normalize(paths_);
  return *this;
}

Path& Path::Append(const std::string& path) {
  return Append(Path(path));
}

Path& Path::Set(const StringArray_t path) {
  paths_ = Normalize(path);
  return *this;
}

Path& Path::Set(const std::string& path) {
  return Set(Split(path));
}

Path Path::Parent() const {
  Path out;
  out.paths_ = paths_;
  if (out.paths_.size())
    out.paths_.pop_back();
  return out;
}

std::string Path::Basename() const {
  if (paths_.size())
    return paths_.back();
  return std::string();
}

std::string Path::Join() const {
  return Range(paths_, 0, paths_.size());
}

std::string Path::Range(size_t start, size_t end) const {
  return Range(paths_, start, end);
}

StringArray_t Path::Split() const {
  return paths_;
}

// static
StringArray_t Path::Normalize(const StringArray_t& paths) {
  StringArray_t path_out;

  for (size_t index = 0; index < paths.size(); index++) {
    const std::string& curr = paths[index];

    // Check if '/' was used excessively in the path.
    // For example, in cd Desktop/////
    if (curr == "/" && index != 0)
      continue;

    // Check for '.' in the path and remove it
    if (curr == ".")
      continue;

    // Check for '..'
    if (curr == "..") {
      // If the path is empty, or "..", then add ".."
      if (path_out.empty() || path_out.back() == "..") {
        path_out.push_back(curr);
        continue;
      }

      // If the path is at root, "/.." = "/"
      if (path_out.back() == "/") {
        continue;
      }

      // if we are already at root, then stay there (root/.. -> root)
      if (path_out.back() == "/") {
        continue;
      }

      // otherwise, pop off the top path component
      path_out.pop_back();
      continue;
    }

    // By now, we should have handled end cases so just append.
    path_out.push_back(curr);
  }

  // If the path was valid, but now it's empty, return self
  if (path_out.empty())
    path_out.push_back(".");

  return path_out;
}

// static
std::string Path::Join(const StringArray_t& paths) {
  return Range(paths, 0, paths.size());
}

// static
std::string Path::Range(const StringArray_t& paths, size_t start, size_t end) {
  std::string out_path;
  size_t index = start;

  if (end > paths.size())
    end = paths.size();

  // If this is an absolute path, paths[0] == "/". In this case, we don't want
  // to add an additional / separator.
  if (start == 0 && end > 0 && paths[0] == "/") {
    out_path += "/";
    index++;
  }

  for (; index < end; index++) {
    out_path += paths[index];
    if (index < end - 1)
      out_path += "/";
  }

  return out_path;
}

// static
StringArray_t Path::Split(const std::string& path) {
  StringArray_t path_split;
  StringArray_t components;

  sdk_util::SplitString(path, '/', &path_split);

  if (path[0] == '/')
    components.push_back("/");

  // Copy path_split to components, removing empty path segments.
  for (StringArray_t::const_iterator it = path_split.begin();
       it != path_split.end();
       ++it) {
    if (!it->empty())
      components.push_back(*it);
  }
  return components;
}

Path& Path::operator=(const Path& p) {
  paths_ = p.paths_;
  return *this;
}

Path& Path::operator=(const std::string& p) {
  return Set(p);
}

}  // namespace nacl_io
