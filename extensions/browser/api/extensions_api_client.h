// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef EXTENSIONS_BROWSER_API_EXTENSIONS_API_CLIENT_H_
#define EXTENSIONS_BROWSER_API_EXTENSIONS_API_CLIENT_H_

#include <map>

#include "base/memory/ref_counted.h"
#include "base/memory/scoped_ptr.h"
#include "extensions/browser/api/declarative/rules_registry.h"
#include "extensions/browser/api/storage/settings_namespace.h"

class GURL;

template <class T>
class ObserverListThreadSafe;

namespace content {
class BrowserContext;
}

namespace extensions {

class AppViewGuestDelegate;
class ExtensionOptionsGuest;
class ExtensionOptionsGuestDelegate;
class MimeHandlerViewGuest;
class MimeHandlerViewGuestDelegate;
class WebViewGuest;
class WebViewGuestDelegate;
class WebViewPermissionHelper;
class WebViewPermissionHelperDelegate;
class WebRequestEventRouterDelegate;
class SettingsObserver;
class SettingsStorageFactory;
class ValueStoreCache;

// Allows the embedder of the extensions module to customize its support for
// API features. The embedder must create a single instance in the browser
// process. Provides a default implementation that does nothing.
class ExtensionsAPIClient {
 public:
  // Construction sets the single instance.
  ExtensionsAPIClient();

  // Destruction clears the single instance.
  virtual ~ExtensionsAPIClient();

  // Returns the single instance of |this|.
  static ExtensionsAPIClient* Get();

  // Storage API support.

  // Add any additional value store caches (e.g. for chrome.storage.managed)
  // to |caches|. By default adds nothing.
  virtual void AddAdditionalValueStoreCaches(
      content::BrowserContext* context,
      const scoped_refptr<SettingsStorageFactory>& factory,
      const scoped_refptr<ObserverListThreadSafe<SettingsObserver> >& observers,
      std::map<settings_namespace::Namespace, ValueStoreCache*>* caches);

  // Creates the AppViewGuestDelegate.
  virtual AppViewGuestDelegate* CreateAppViewGuestDelegate() const;

  // Returns a delegate for ExtensionOptionsGuest. The caller owns the returned
  // ExtensionOptionsGuestDelegate.
  virtual ExtensionOptionsGuestDelegate* CreateExtensionOptionsGuestDelegate(
      ExtensionOptionsGuest* guest) const;

  // Creates a delegate for MimeHandlerViewGuest.
  virtual scoped_ptr<MimeHandlerViewGuestDelegate>
      CreateMimeHandlerViewGuestDelegate(MimeHandlerViewGuest* guest) const;

  // Returns a delegate for some of WebViewGuest's behavior. The caller owns the
  // returned WebViewGuestDelegate.
  virtual WebViewGuestDelegate* CreateWebViewGuestDelegate (
      WebViewGuest* web_view_guest) const;

  // Returns a delegate for some of WebViewPermissionHelper's behavior. The
  // caller owns the returned WebViewPermissionHelperDelegate.
  virtual WebViewPermissionHelperDelegate*
      CreateWebViewPermissionHelperDelegate (
          WebViewPermissionHelper* web_view_permission_helper) const;

  // TODO(wjmaclean): Remove this as soon as rules_registry_service.* moves to
  // extensions/browser/api/declarative/.
  virtual scoped_refptr<RulesRegistry> GetRulesRegistry(
      content::BrowserContext* browser_context,
      const RulesRegistry::WebViewKey& webview_key,
      const std::string& event_name);

  // Creates a delegate for WebRequestEventRouter.
  virtual WebRequestEventRouterDelegate* CreateWebRequestEventRouterDelegate()
      const;

  // NOTE: If this interface gains too many methods (perhaps more than 20) it
  // should be split into one interface per API.
};

}  // namespace extensions

#endif  // EXTENSIONS_BROWSER_API_EXTENSIONS_API_CLIENT_H_
