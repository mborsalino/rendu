import os
import os.path as osp
import shutil


class HtmlDoc(object):
    """
    Class that represents an HTML document and provides methods to add basic
    HTML elements to it.
    """

    def __init__(self, title=None):
        self.title = title
        self.html = ('<!DOCTYPE html\n'
                     '<html>\n')
        if title is not None:
            self.html += ('<head>\n'
                          '<title>%s</title>\n'
                          '</head>\n'%title)
        self.html += '<body>\n'
        self.img_list = []


    def add_h1(self, txt):
        self.html += '<h1>%s</h1>\n'%txt


    def add_h2(self, txt):
        self.html += '<h2>%s</h2>\n'%txt


    def add_h3(self, txt):
        self.html += '<h3>%s</h3>\n'%txt


    def add_image(self, img_path, embedded=True, caption=None):
        """
        Add image to HTML document.

        Parameters:
        ------
        img_path: str
            The path of the image file (jpg/jpeg/png only)
        embedded: bool
            If True (default), embed image into html (base64-encoded)
            If False, create img folder containing image and point to folder
        caption: str
            If not None, the caption to be inserted at the bottom of the image
        """
        # Arg check
        if not osp.exists(img_path):
            raise ArgError('Invalid path %s'%img_path)
        root, img_ext = osp.splitext(img_path)

        if img_ext.lower() not in ('.png', '.jpg', '.jpeg'):
            raise ArgError('Only png/jpeg/jpg file types are supported')

        if embedded:
            fh = open(img_path, 'rb')
            stream = BytesIO(fh.read())
            fh.close()
            encoded_str = base64.b64encode(stream.getvalue()).decode('utf-8')

            self.html += "<figure>\n"
            self.html +=  "<img src='data:image/"
            if img_ext.lower() in ('jpg', 'jpeg'):
                self.html +=  "jpeg;"
            else:
                self.html +=  "png;"
            self.html += 'base64,'
            self.html += encoded_str
            self.html += "'>\n"
            if caption is not None:
                self.html += '<figcaption>%s</figcaption>\n'%caption
            self.html += "</figure>\n"
        else:
            self.html +=  "<img src='img/%s'>\n"%osp.basename(img_path)
            self.img_list.append(img_path)


    def save(self, out_path):
        """
        Save the document to the specified output file.
        """

        # Check that the path exists
        out_dir = osp.dirname(out_path)
        if len(out_dir) == 0:
            out_dir = '.'
        if  not osp.exists(out_dir):
            raise ArgError('The directory %s does not exist'%out_dir)

        self.html += ('</body>\n'
                      '</html>')

        fh = open(out_path, 'w')
        fh.write(self.html)
        fh.close()

        if len(self.img_list) > 0:
            img_dir = osp.join(out_dir, 'img')
            os.makedirs(img_dir, exist_ok=True)
            for fpath in self.img_list:
                shutil.copy(fpath, img_dir)




