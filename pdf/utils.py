import os
from zipfile import ZipFile
from latex import build_pdf

from csedu_research_hub.settings import MEDIA_ROOT

def extract_zip(zip_path: str):
    """
    Extracts a zip file to a destination path.
    """
    file_timestamp = zip_path.split('/')[-1].split('.')[0]
    dest_path = os.path.join(MEDIA_ROOT, "build_dir", file_timestamp)
    with ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dest_path)
    return dest_path


def make_pdf(build_dir: str, pdf_name: str, main_aux_file: str):
    """
    Creates a PDF from a build directory.
    """
    pdf_path = os.path.join(build_dir, main_aux_file)
    print(pdf_path, pdf_name, main_aux_file)
    pdf = build_pdf(open(pdf_path), texinputs=[build_dir, ""])
    pdf.save_to(os.path.join(MEDIA_ROOT, "pdf", pdf_name+".pdf"))
    return pdf_path