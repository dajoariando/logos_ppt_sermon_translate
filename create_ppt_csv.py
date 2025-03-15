from pptx import Presentation
from add_page import add_page
from translate_csv import translate_csv

def create_ppt_csv(input_csv, output_pptx):
    # create presentation
    prs = Presentation()
    prs.core_properties.author = "David Ariando"

    text_indo, text_eng = translate_csv(input_csv)

    for i in range(len(text_indo)):
        prs = add_page(prs, text_indo[i], text_eng[i])

    # save the file
    prs.save(output_pptx)

# Example usage
create_ppt_csv("input_english_indo.csv", "output_csv.pptx")
