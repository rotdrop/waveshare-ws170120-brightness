# WaveShare WS170120 Brightness

## Host to device

The brightness control seem to be located in the last 38 "left-over"
(wireshark notation) bytes. The URB for setting brightness to 10 looks
like this:

- Standard URB headers:
```
0000   40 82 7e b4 c4 07 ff ff 53 01 01 03 01 00 2d 00   @.~.....S.....-.
0010   ff d3 aa 65 00 00 00 00 60 6e 06 00 8d ff ff ff   ...e....`n......
0020   26 00 00 00 26 00 00 00 00 00 00 00 00 00 00 00   &...&...........
0030   01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
```

- "leftover" capture data:
```
0000   04 aa 01 00 00 00 64 00 00 00 00 00 00 00 00 00   ......d.........
0010   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0020   00 00 00 00 00 00                                 ......
```

The brightness value is located in byte number 7 of the leftover data
and seems to be a value in percent. Howerver, at least the user-space
tools like `Raspi_USB_Backlight_nogui` on support 10 distinct steps
for the brightness. The other non-zero bytes at the start of the
leftover data are always the same; perhaps some "magic fourc" or so.

## Device answer

The device seemingly answers just with a standard handshake without additional data. It would be nice to be able to query the actual brightness, but this does not seem to be possible(?).

```
0000   c0 39 cc f0 c4 07 ff ff 43 01 01 03 01 00 2d 3e   .9......C.....->
0010   67 d3 aa 65 00 00 00 00 f6 1f 0f 00 00 00 00 00   g..e............
0020   26 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   &...............
0030   01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
```

## Query the current brightness

At least the tools from Waveshare do not query the current setting, so
this might not be possible, unfortunately. Of course, one can write a
system service which maintains the state of the last set brightness
and e.g. implement a dbus service to query and set it.
