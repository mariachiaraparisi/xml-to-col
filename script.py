import csv
import xml.etree.ElementTree as ET
import os
import glob

latin_namespaces = {"tei": "http://www.tei-c.org/ns/1.0"}

input_dir = "./input"
output_dir = "./output"
error_list = []


def get_latin_output(root, output):
    chapters = (
        root.find("tei:text", latin_namespaces)
        .find("tei:body", latin_namespaces)
        .findall("tei:ab", latin_namespaces)
    )

    for chapter in chapters:
        words = chapter.findall("tei:w", latin_namespaces)
        for word in words:
            output.writerow(
                [
                    word.text,
                    word.attrib["lemma"],
                    word.attrib["pos"],
                    word.attrib["msd"],
                ]
            )


def get_greek_output(root, output):
    sentences = root.findall("s")

    for sentence in sentences:
        texts = sentence.findall("t")
        for text in texts:
            lemmas = text.find("l")

            output.writerow(
                [
                    text.find("f").text,
                    getattr(lemmas.find("l1"), "text", ""),
                    getattr(lemmas.find("l2"), "text", ""),
                    text.attrib["o"][:1],
                    text.attrib["o"][1:],
                    lemmas.attrib["i"] if "i" in lemmas.attrib else "",
                ]
            )


def run_file(input_path):
    try:
        root = ET.parse(input_path).getroot()

        if "text-cts" in root.attrib:
            greek = True
            file_id = root.attrib["text-cts"]
        else:
            greek = False
            file_id = root.find("tei:teiHeader", latin_namespaces).attrib["n"]

    except:
        error_list.append(input_path)
        return

    output_path = f"{output_dir}/{file_id}-parsed_lemmatised.tsv"

    if os.path.exists(output_path):
        print(f"Skipping... file already exists at path: {output_path}")
    else:
        print(f"{input_path} -> {output_path}")

        with open(output_path, "w") as file_output:
            tsv_output = csv.writer(file_output, delimiter="\t")

            if greek:
                get_greek_output(root, tsv_output)
            else:
                get_latin_output(root, tsv_output)


if not os.path.exists(output_dir):
    print(f"Creating output directory: {output_dir}")
    os.makedirs(output_dir)

print("Parsing and writing files:")

for filepath in glob.glob(f"{input_dir}/*.xml"):
    run_file(filepath)

if len(error_list) > 0:
    print("The following files failed to parse:")
    for file in error_list:
        print(file)
