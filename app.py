try:
    import werpy
    import gradio as gr
except ImportError as e:
    print(f"An error occurred while importing modules: {str(e)}")
    exit()

def word_error_rate(reference, hypothesis):
    try:
        normalized_reference = werpy.normalize(reference)
        normalized_hypothesis = werpy.normalize(hypothesis)
        wer_result = werpy.wer(normalized_reference, normalized_hypothesis)
        return wer_result
    except Exception as e:
        return f"An error occurred: {str(e)}"

title = "Word Error Rate Calculator"
description = "A simple application to quickly calculate the Word Error Rate (WER) powered by <a href='https://pypi.org/project/werpy/'>werpy</a>."

# Define the input and output interfaces
input_reference = gr.Textbox(lines=2, label="Input Reference Text")
input_hypothesis = gr.Textbox(lines=2, label="Input Hypothesis Text")
output_wer = gr.Number(label="Word Error Rate")

iface = gr.Interface(
    fn = word_error_rate, 
    inputs = [input_reference, input_hypothesis], 
    outputs = output_wer,
    title = title,
    description = description
)
iface.launch()
