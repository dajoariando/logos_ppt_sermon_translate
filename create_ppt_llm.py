from pptx import Presentation
from add_page import add_page
from translate_csv import translate_csv
from translate_ollama import translate_ollama
from translate_chatgpt import translate_chatgpt
from parse_txt import parse_txt
from parse_txt_dual_enter import parse_txt_dual_enter

def create_ppt_llm(input_file, output_file):
    # create presentation
    prs = Presentation()
    prs.core_properties.author = "David Ariando"

    # set slide size to 16:9 format
    prs.slide_width = 12192000
    prs.slide_height = 6858000

    # text_indo,text_eng = translate_csv("input_file") # takes csv file with two columns as am input
    # text_eng = parse_txt(input_file) # uses a newline character as page separator
    text_eng = parse_txt_dual_enter(input_file) # uses two newline characters as page separator

    # add the text to the presentation
    for i in range(len(text_eng)):
        translation_indo = translate_chatgpt(text_eng[i]) # translate using ChatGPT (requires API access)
        # translation_indo = translate_ollama(text_eng[i]) # translate using Ollama (requires local server)
        prs = add_page(prs, translation_indo, text_eng[i]) # add a line to the presentation and comment to comment section

        # Calculate and print the process percentage
        percentage = (i+1) / len(text_eng) * 100
        print(f"Progress:{percentage:3.0f} %")

    # save the file
    prs.save(output_file)

# Example usage
# create_ppt_llm("input_sample.txt", "output_llm.pptx")
