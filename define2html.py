from lxml import etree
from pathlib import Path
import argparse

"""
Example:
    python3 define2html.py -d ./define.xml -o ./define.html -x ./define2-1.xsl
"""

def transform_xml_to_html(args):
    """
    Transforms a define.xml to an HTML file using the define2-1 XSL stylesheet.
    """
    xml_tree = etree.parse(args.define)
    xsl_tree = etree.parse(args.xsl)
    transform = etree.XSLT(xsl_tree)
    result_tree = transform(xml_tree)

    with open(args.out, 'wb') as f:
        f.write(etree.tostring(result_tree, pretty_print=True))

def set_cmd_line_args():
    """
    get the command-line arguments needed to convert the define.xml input file into HTML using XSL
    :return: return the argparse object with the command-line parameters
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--define", help="path and file name of the define.xml file", required=False,
                        dest="define", default=str(Path(__file__).parent.joinpath("define.xml")))
    parser.add_argument("-o", "--out", help="path and file name of HTML file to create", required=False,
                        dest="out", default=str(Path(__file__).parent.joinpath("define.html")))
    parser.add_argument("-x", "--xsl", help="path and file name of the stylesheet", required=False,
                        dest="xsl", default=(Path(__file__).parent.joinpath("define2-1.xsl")))
    args = parser.parse_args()
    return args

def main():
    """ main driver method that generates HTML from define.xml using the define style sheet """
    args = set_cmd_line_args()
    transform_xml_to_html(args)

if __name__ == "__main__":
    main()
