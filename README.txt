An introduction to using Fiati
==============================

Fiati is a font containing musical symbols intended for use in text-based applications such as word processors, text editors, desktop publishers and musical scoring software.

Fiati is licensed under the SIL Open Font License (http://scripts.sil.org/), which means it is free to use, redistribute, and modify, but please do respect the conditions set out in the license.


Glyph repertoire
================

Fiati uses the Private Use Area of Unicode's Basic Multilingual Plane (U+E000 through U+FFFF) to encode all of the included symbols. This means that the symbols cannot be typed by using the alphanumeric keys on your computer's keyboard on their own.


Setting up for Unicode input
============================

Detailed instructions for how to enable Unicode input on all operating systems are beyond the scope of this document. SIL provides an excellent page (http://scripts.sil.org/cms/scripts/page.php?item_id=inputtoollinks) with links to information and tools for Windows, MacOS and Linux. In this document some basic instructions are included, but you may need to refer to other resources for help with your operating system and application of choice.


Windows
=======
There are multiple ways to type Unicode characters on Windows. Here are three methods you can try:

Method 1: hexadecimal input followed by `Alt`
========
On Windows, some applications, such as Microsoft Word (part of the Microsoft Office suite) and WordPad (included with every Windows installation), have support for converting a typed alphanumeric sequence into a single Unicode character.

The Unicode code point for a flute base diagram in Fiati is U+EC40, which is a hexadecimal number (60480 in decimal). To enter this character in Word or WordPad, type `EC40` followed by `Alt+X` (hold the `Alt` key and then hit the `X` key). The typed characters **EC40** will be replaced by a single character, which may display as an empty rectangle or a rectangle containing **?**. Select this character and change the font to Fiati, and the flute base diagram appears.

Although Unicode code points are normally written in the form U+EC40, you can ignore the "U+" part when entering the code point in this and the following method.

Method 2: `Alt` + hexadecimal input
========
If the application you are using does not support the kind of conversion described above, you can enable Unicode input by holding `Alt`, then typing `+` **on the numeric keypad**, then typing the hexadecimal number on the numeric keypad, before finally releasing `Alt`. For example, to type the flute base diagram (U+EC40), hold `Alt`, type keypad `+`, then `EC40`, then release `Alt`. Again, if Fiati is not the selected font, you may see an empty rectangle or a rectangle containing **?**. Select this character and change the font to Fiati, and the flute base diagram appears.

Method 3: Character Map
========
The built-in Character Map application can copy any Unicode character to the system clipboard so that it can be pasted into another application. To run Character Map, click the `Start` button or hit the `Windows` key on your keyboard, then type `charmap` and hit `Return`. Character Map will run.

In Character Map, choose **Fiati** from the **Font** menu at the top of the window. Switch on the **Advanced view** checkbox at the bottom of the window, which makes extra options appear. Choose **Unicode** from the **Character set** menu, then choose **Unicode Subrange** from the bottom of the **Group by** menu. A further pop-up window appears, captioned **Group By**, showing a list of Unicode subranges; choose **Private Use Characters** from the bottom of the list. (You can then close the **Group By** window if you wish.)

The grid that occupies the main part of the Character Map window now displays all of the symbols in Fiati (unfortunately, it is not possible to enlarge the display, so they are rather small). Once you have located the character you require, either select it with the mouse and click **Select** or double-click it, and it is added to the **Characters to copy** edit control. Click **Copy** to copy the contents of **Characters to copy** to the clipboard, then switch to the application into which you want to paste the text, and choose `Edit` ▸ `Paste`, or type `Ctrl+V`.

Other methods
=============
You may wish to experiment with third-party utilities that can assist with locating and inserting Unicode characters. No recommendation or warranty is implied by listing these free utilities, which you may try at your own risk:

* CatchChar (http://helpingthings.com/index.php/insert-unicode-characters) allows you to add commonly-used Unicode characters to a menu that can be triggered from within any application via a keyboard shortcut.
* BabelMap (http://www.babelstone.co.uk/Software/BabelMap.html) is an advanced alternative to Windows's built-in Character Map application.

MacOS
=====
For Mac computers running MacOS, the simplest method to insert arbitrary Unicode characters is using the provided Unicode Hex Input input method. To enable it:

* In System Preferences, choose **Keyboard**.
* On the **Keyboard** tab, switch on **Show Keyboard & Character Viewers in menu bar**. When switched on, you will see a national flag corresponding to your computer keyboard's normal language and/or layout appear in the menu bar to the left of the Spotlight icon.
* On the **Input Sources** tab, click **+**, and in the sheet that appears, select **Others** in the left-hand list, then select **Unicode Hex Input** in the right-hand list, then click **Add** to close the sheet.
* Ensure **Show Input menu in menu bar** is switched on, then close System Preferences.

The Unicode Hex Input input method works in the majority of MacOS applications. To try it out, for example, open a new text document in TextEdit. Fiati does not appear by default in the font menu in TextEdit's toolbar, because it is not an English-language font, so to choose Fiati you must show the Fonts panel by choosing `Format` ▸ `Font` ▸ `Show Fonts` or typing `⌘T`. In the Fonts panel, choose **All fonts** under **Collection**, then choose **Fiati** under **Family**, then close the Fonts panel (type `⌘T` again).

Fiati is now the chosen font (and will now appear in the font menu in TextEdit's toolbar for this document). To type a flute base diagram, which has the code point U+EC40, first choose the **Unicode Hex Input** input method from the input menu in the menu bar. Now hold down `Alt/Option ⌥` and type `EC40` (do not type the "U+" prefix), then release `Alt/Option ⌥`.

If you want to switch between your normal language input method and the Unicode Hex Input method quickly, you can assign a system keyboard shortcut in the **Keyboard** pane of System Preferences. Choose the **Shortcuts** tab, then in the left-hand list choose **Input Sources**. Switch on the checkbox for either or both of **Select the previous input source** and **Select the next input source**, and assign a keyboard shortcut. The default shortcut suggested by MacOS is used for Spotlight by default, so you may wish to assign another shortcut, e.g. `^Space` (`^` is the symbol that corresponds to the `Ctrl` key).


Usage notes for Fiati
=====================

Scale factor
============
Fiati is scaled such that the height of a five-line staff (e.g. U+E014) from the Bravura font is approximately the same as the height of an upper case letter in a regular text font at the same point size. It is designed to be used both in-line, i.e. in the middle of a run of text at the same point size, and on its own, typically at a larger point size. As such, all symbols in Fiati are scaled appropriately to be drawn at the correct size on a five-line staff.

Zero-width characters
=====================
Symbols in Fiati have zero width to allow other musical symbols to be printed on top of them.

All glyphs have zero side-bearings, i.e. the advance width of each glyph is exactly equal to the bounding box of its symbol.

Space characters
================
In order to insert space between symbols, use the following keys:

* Typing `Space` advances the input position by half a space.

Further information
===================
Detailed technical support is not available for the use of Fiati, but if you encounter any problems using this font, please use the issues section within repository or stackoverflow (https://stackoverflow.com) to ask the community about your problem.
