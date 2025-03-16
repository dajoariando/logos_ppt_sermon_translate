from pptx import Presentation
from add_page import add_page
from translate_csv import translate_csv

def create_ppt_csv(input_csv, output_pptx):
    # create presentation
    prs = Presentation()
    prs.core_properties.author = "David Ariando"

    # set slide size to 16:9 format
    prs.slide_width = 12192000
    prs.slide_height = 6858000

    # get the text from the csv file
    text_indo, text_eng = translate_csv(input_csv)

    # add the text to the presentation
    for i in range(len(text_indo)):
        prs = add_page(prs, text_indo[i], text_eng[i])

    # save the file
    prs.save(output_pptx)

# Example usage
# create_ppt_csv("input_sample.csv", "output_csv.pptx")
