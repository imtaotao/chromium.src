// Copyright (c) 2011 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

cr.define('options', function() {

  var OptionsPage = options.OptionsPage;
  var UserImagesGrid = options.UserImagesGrid;
  var ButtonImages = UserImagesGrid.ButtonImages;

  /////////////////////////////////////////////////////////////////////////////
  // ChangePictureOptions class:

  /**
   * Encapsulated handling of ChromeOS change picture options page.
   * @constructor
   */
  function ChangePictureOptions() {
    OptionsPage.call(
        this,
        'changePicture',
        localStrings.getString('changePicturePage'),
        'change-picture-page');
  }

  cr.addSingletonGetter(ChangePictureOptions);

  ChangePictureOptions.prototype = {
    // Inherit ChangePictureOptions from OptionsPage.
    __proto__: options.OptionsPage.prototype,

    /**
     * Initializes ChangePictureOptions page.
     */
    initializePage: function() {
      // Call base class implementation to start preferences initialization.
      OptionsPage.prototype.initializePage.call(this);

      var imageGrid = $('images-grid');
      UserImagesGrid.decorate(imageGrid);

      imageGrid.addEventListener('change', function(e) {
        // Ignore programmatical selection.
        if (!imageGrid.inProgramSelection) {
          // Button selections will be ignored by Chrome handler.
          chrome.send('selectImage', [this.selectedItemUrl || '']);
        }
      });
      imageGrid.addEventListener('activate',
                                 this.handleImageActivated_.bind(this));
      imageGrid.addEventListener('dblclick',
                                 this.handleImageDblClick_.bind(this));

      // Add "Take photo" and "Choose a file" buttons in a uniform way with
      // other buttons.
      imageGrid.addItem(ButtonImages.CHOOSE_FILE,
                        localStrings.getString('chooseFile'),
                        this.handleChooseFile_.bind(this));
      imageGrid.addItem(ButtonImages.TAKE_PHOTO,
                        localStrings.getString('takePhoto'),
                        this.handleTakePhoto_.bind(this));

      // Profile image data.
      this.profileImage_ = imageGrid.addItem(
          ButtonImages.PROFILE_PICTURE,
          localStrings.getString('profilePhotoLoading'));

      // Old user image data (if present).
      this.oldImage_ = null;
    },

    /**
     * Called right after the page has been shown to user.
     */
    didShowPage: function() {
      $('images-grid').updateAndFocus();
      chrome.send('getSelectedImage');
    },

    /**
     * Called right before the page is hidden.
     */
    willHidePage: function() {
      if (this.oldImage_) {
        $('images-grid').removeItem(this.oldImage_);
        this.oldImage_ = null;
      }
    },

    /**
     * Closes current page, returning back to Personal Stuff page.
     * @private
     */
    closePage_: function() {
      OptionsPage.navigateToPage('personal');
    },

    /**
     * Handles "Take photo" button activation.
     * @private
     */
    handleTakePhoto_: function() {
      chrome.send('takePhoto');
      this.closePage_();
    },

    /**
     * Handles "Choose a file" button activation.
     * @private
     */
    handleChooseFile_: function() {
      chrome.send('chooseFile');
      this.closePage_();
    },

    /**
     * Handles image activation (by pressing Enter).
     * @private
     */
    handleImageActivated_: function() {
      switch ($('images-grid').selectedItemUrl) {
        case ButtonImages.TAKE_PHOTO:
          this.handleTakePhoto_();
          break;
        case ButtonImages.CHOOSE_FILE:
          this.handleChooseFile_();
          break;
        default:
          this.closePage_();
          break;
      }
    },

    /**
     * Handles double click on the image grid.
     * @param {Event} e Double click Event.
     */
    handleImageDblClick_: function(e) {
      // If an image is double-clicked and not the grid itself, close the page.
      if (e.target.id != 'images-grid')
        this.closePage_();
    },

    /**
     * URL of the current user image.
     * @type {string}
     */
    get currentUserImageUrl() {
      return 'chrome://userimage/' + PersonalOptions.getLoggedInUserEmail() +
          '?id=' + (new Date()).getTime();
    },

    /**
     * Adds or updates old user image taken from file/camera (neither a profile
     * image nor a default one).
     * @private
     */
    setOldImage_: function() {
      var imageGrid = $('images-grid');
      var url = this.currentUserImageUrl;
      if (this.oldImage_) {
        this.oldImage_ = imageGrid.updateItem(this.oldImage_, url);
      } else {
        this.oldImage_ = imageGrid.addItem(url, undefined, undefined, 3);
        imageGrid.selectedItem = this.oldImage_;
      }
    },

    /**
     * Updates user's profile image.
     * @param {string} imageUrl Profile image, encoded as data URL.
     * @param {boolean} select If true, profile image should be selected.
     * @private
     */
    setProfileImage_: function(imageUrl, select) {
      var imageGrid = $('images-grid');
      this.profileImage_ = imageGrid.updateItem(
          this.profileImage_, imageUrl, localStrings.getString('profilePhoto'));
      // If there is no previous selection, select it.
      if (select)
        imageGrid.selectedItem = this.profileImage_;
    },

    /**
     * Selects user image with the given URL.
     * @param {string} url URL of the image to select.
     * @private
     */
    setSelectedImage_: function(url) {
      $('images-grid').selectedItemUrl = url;
    },

    /**
     * Appends received images to the image grid.
     * @param {Array.<string>} images An array of URLs to user images.
     * @private
     */
    setUserImages_: function(images) {
      var imageGrid = $('images-grid');
      for (var i = 0, url; url = images[i]; i++) {
        imageGrid.addItem(url);
      }
    },
  };

  // Forward public APIs to private implementations.
  [
    'setOldImage',
    'setProfileImage',
    'setSelectedImage',
    'setUserImages',
  ].forEach(function(name) {
    ChangePictureOptions[name] = function(value1, value2) {
      ChangePictureOptions.getInstance()[name + '_'](value1, value2);
    };
  });

  // Export
  return {
    ChangePictureOptions: ChangePictureOptions
  };

});

