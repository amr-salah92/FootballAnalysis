import pandas as pd
from fpdf import FPDF

class DataExporter:
    @staticmethod
    def to_csv(data, filename):
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        
    @staticmethod
    def to_pdf(data, filename):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Football Analysis Report", ln=1, align="C")
        # Add table
        pdf.output(filename)