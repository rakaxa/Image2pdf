# -*- coding: utf-8 -*-  

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import cm
from PIL import Image
import os
import sys
import glob

class Img():
  def blend_value(self, under, over, a):
    return (over*a + under*(255-a)) / 255


  def blend_rgba(self, under, over):
    return tuple([self.blend_value(under[i], over[i], over[3]) for i in (0,1,2)] + [255])


  def RGBA2RGB(self, image):
    white = (255, 255, 255, 255)
    p = image.load()
    for y in range(image.size[1]):
      for x in range(image.size[0]):
        p[x,y] = self.blend_rgba(white, p[x,y])
    return


  def read(self, path):
    image_path = os.path.normpath(path)
    if os.path.exists(image_path):
      image = Image.open(image_path)
    else:
      image = None
    return image



class Keyword():
  def get(self):
    if len(sys.argv) != 2:
      return None
    else:
      return sys.argv[1]


class PDF():
  def setparam(self, pdfFile):
    pdfFile.saveState()
    pdfFile.setAuthor("")
    pdfFile.setSubject("画像たち")
    pdfFile.setPageSize((21.0*cm,29.7*cm))
    
    return


  def make(self, pdfFile, image):
    pdfFile.setPageSize((image.size[0],image.size[1]))
    pdfFile.drawInlineImage(image,0,0)
    pdfFile.showPage()
    
    return


  def done(self, pdfFile):
    pdfFile.save()

    return


def main():

  pdf = PDF()
  img = Img()
  kwd = Keyword()

  keyword = kwd.get()
  if keyword == None:
    print('usage : > python %s dirname' % sys.argv[0])
    quit()

#  pdfFile = canvas.Canvas("./" + keyword + ".pdf")
  pdfFile = canvas.Canvas(unicode(keyword, 'shift-jis') + ".pdf")  # for Windows
  pdf.setparam(pdfFile)

  search_path = os.path.normpath("./" + keyword + "/*")
  for file in glob.glob(search_path):
    image = img.read(file)
    if image.mode == 'RGBA':
      img.RGBA2RGB(image)
    pdf.make(pdfFile, image)
  pdf.done(pdfFile)
  print("Finished.")

if __name__ == "__main__":
  sys.exit(main())
