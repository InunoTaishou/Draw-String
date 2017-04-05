# Draw-String
Draw a formatted string in a defined rect area using pygame.
Strings can be a combination of (horizontally) aligned left, center, right and (vertically) aligned top, center, bottom

String will be drawn using the draw_string function inside the Graphics.py. Parameters need a surface to draw on, the string to draw (\n character is supported and will draw the line on the next line), a pygame.rect area, pygame.font, and the color to color text.

Main function to use is in the Graphics.py file

draw_string requires
  surface to draw on (surface returned from pygame.display.set_mode)
  string to draw (\n character is supported)
  rect area (rect returned from pygame.Rect(x, y, width, height))
  font object (font returned from pygame.font)
  format object (created using Graphycs.StringFormat. default values are left and top)
  color (color created using the R, G, B values, ex. (255, 255, 255) for white)

Example can be found in main.py
