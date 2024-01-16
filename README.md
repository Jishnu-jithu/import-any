<p align="center">
  <img src="https://github.com/Jishnu-jithu/import-any/assets/145359279/ca33b975-63ad-49db-97ca-c0ddb9a60af4">
</p>

<p align="center">
  <kbd>
    <br>
    <a href="https://www.blendermarket.com/products/import-any">Get it on BlenderMarket</a>
    <br>
    <br>
  </kbd>
</p>

# Import Any - Blender Add-On

**Import Any** is a versatile Blender add-on that enables you to seamlessly import a variety of file formats, making your workflow more flexible and efficient. The add-on supports a wide range of formats, making it a valuable tool for 3D artists and developers.

## Features

- Seamless Import of Any File Format - With Import Any, enjoy the flexibility of importing a multitude of file formats effortlessly. Access all supported formats through a menu.

- Copy-Paste File Path Import - Efficiency meets simplicity! Copy the file path directly from your file explorer and paste it into Blender.

- Batch Importing Capabilities - Import Any addon allows you to batch import, saving you valuable time and effort.

## Supported Formats

fbx, obj, stl, gltf, glb, dae, usd, usda, usdc, usdz, bvh, x3d, 3ds, ply, pdb, dxf, chan, jpg, jpeg, png, mp4, psd, py, txt.

## Installation

1. Download the add-on ZIP file.
2. Open Blender and navigate to Edit > Preferences > Add-ons.
3. Click "Install" and select the downloaded ZIP file.
4. Enable the "Import-Export: Import Any" add-on.

## Usage

#### Method 1: Import from Import Any Menu

1. Open Blender.
2. Go to **File > Import > Import Any** or press `Shift+V` to open the file selector.
3. Choose the file(s) you want to import.
4. Optionally, enable "Create Collection" to group objects into separate collections based on file types.
5. Click "Import."

#### Method 2: Import from Clipboard

1. Copy the file path(s) from Windows Explorer.

   - Right-click on the file(s) > Copy as path.
   - Alternatively, select the file(s), `Ctrl+Shift+C`
3. In Blender, press `V` to open the menu or `Alt+v` to open then popup dialog.
4. Select the model name from the menu.

#### Import Menu Location Preferences

You can customize the placement of the Import Any menu:

1. Go to Edit > Preferences > Add-ons > Import Any.
2. In the Import Menu Location section, choose one of the following options:
   
   - **File Menu:** Display the Import Any option in the main File menu.
   - **Import Submenu:** Display the option in the Import submenu of the File menu.
   - **Both Menus:** Display the option in both the main File menu and the Import submenu.
   - **Above Import Menu:** Display the option at the top of the Import menu.

---

## Changelog

### Version 1.3

#### Added Features:
- **Import from Clipboard Popup**: A new popup has been added to import from the clipboard. This addresses some restrictions of the clipboard menu, such as closing instantly when importing one model out of multiple files, or changing settings like turning on/off 'create collection'. With the new popup, you can import all files without interruption and adjust the offset of imported models.

- **File Path and Size Tooltip**: We’ve added a tooltip that displays the file path and size when you hover over the filenames in the popup and menu. This provides more information about the files you’re working with, right at your fingertips.

#### Improvements:
- **Import Status Indication**: The clipboard menu now shows a checkmark icon if a file has been imported. This function tracks the file name and the collection name, so it will not work if a collection was not created when importing. An error icon will be displayed if a file fails to import.

#### Bug Fixes:
- **Model Collection Assignment**: Fixed a bug that caused imported models to move to the default collection (Collection).

https://github.com/Jishnu-jithu/import-any/assets/145359279/4a244fd9-fb25-4df9-8b27-e15e79048d62

---

### Version 1.2

#### Added Features:
- **Offset Option for Imported 3D Models**: We’ve added a new feature that allows you to change the offset of each 3D model imported. This means you can now specify the position of your imported models along the X, Y, or Z axis. This is particularly useful when importing multiple models at once, as it helps prevent overlapping of models. You can set the default settings for this feature in the add-on preferences. Alternatively, you can change the settings from the ‘Import from Clipboard’ panel located in View 3D > Sidebar > Tool.

#### Improvements:
- **Import Status Indication**: We’ve made several improvements to the user interface to make it more intuitive and user-friendly. Now, it’s easier than ever to import your 3D models.
- **Better Error Handling**: We’ve improved the error handling in the add-on. Now, if an error occurs during the import process, the add-on will provide a more descriptive error message, making it easier for you to troubleshoot any issues.
  
---

### Version 1.1

#### Added Features:
- **Create Collection**: This feature allows users to import models into their own collections. When importing multiple models, each model will be placed in a separate collection. This helps in better organization and management of models, especially when dealing with a large number of imports. The feature can be toggled on or off from the add-on preferences.

#### Improvements:
- **Clipboard Import Menu**: The import menu has been enhanced for better user experience. It now includes an option to import all valid paths from the clipboard in one go, improving efficiency. Additionally, the menu dynamically shows or hides the ‘Create Collection’ option based on the user’s preference, providing a cleaner interface.
