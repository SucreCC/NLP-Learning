from reportlab.lib import colors, pagesizes, utils
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from book import Book, ContentType
from utils import LOG

class Writer:
    def __init__(self):
        pass

    def save_translated_book(self, book: Book, output_file_path: str = None, file_format: str = "PDF"):
        if file_format.lower() == "pdf":
            self.save_translated_book_pdf(book, output_file_path)
        elif file_format.lower() == "markdown":
            self.save_translated_book_markdown(book, output_file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_format}")

    def save_translated_book_pdf(self, book, output_file_path):
        if output_file_path is None:
            output_file_path = book.pdf_file_path.replace('.pdf', f'_translated.pdf')
        LOG.info(f"pdf_file_path: {book.pdf_file_path}")
        LOG.info(f"开始翻译: {output_file_path}")

        font_path = "../fonts/simsum.ttc"
        pdfmetrics.registerFont(TTFont("SimSun", font_path))

        simsun_style = ParagraphStyle('SimSun', fontName='SimSun', fontSize=12, leading=14)
        doc = SimpleDocTemplate(output_file_path, pagesize=pagesizes.letter)
        styles = getSampleStyleSheet()
        story = []

        for page in book.pages:
            for content in page.contents:
                if content.content_type == ContentType.TEXT:
                    text = content.translation
                    para = Paragraph(text, simsun_style)
                    story.append(para)
                elif content.content_type == ContentType.TABLE:
                    table = content.translation
                    table_style = TableStyle([
                        ('BACKGROUND', (0,0), (1,0), colors.grey),
                        ('TEXTCOLOR', (0,0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                        ('FONTNAME', (0,0), (0,0), 'SimSum'),
                        ('FONTSIZE', (0,0), (-1, 0), 14),
                        ('BOTTOMPADDING', (0,0), (-1,0), 12),
                        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
                        ('FONTNAME', (0,1), (-1,-1), 'SimSun'),
                        ('GRID', (0,0), (-1,-1), 1, colors.black)
                    ])
                    pdf_table = Table(table.values.tolist())
                    pdf_table.setStyle(table_style)
                    story.append(pdf_table)


            if page != book.pages[-1]:
                story.append(PageBreak())
        doc.build(story)
        LOG.info(f"翻译完成：{output_file_path}")


    def save_translated_book_markdown(self, book, output_file_path):
        if output_file_path is None:
            output_file_path = book.pdf_file_path.replace('.pdf', f'_translated.md')

        LOG.info(f"pdf_file_path: {book.pdf_file_path}")
        LOG.info(f"开始翻译: {output_file_path}")

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for page in book.pages:
                for content in page.contents:
                    if content.status:
                        if content.content_type == ContentType.TEXT:
                            text = content.translation
                            output_file.write(text + '\n\n')

                        elif content.content_type == ContentType.TABLE:
                            table = content.translation
                            header = '| ' + ' | '.join(str(column) for column in table.columns) + ' |' + '\n'
                            separator = '| ' + ' | '.join(['---'] * len(table.columns)) + ' |' + '\n'
                            body = '\n'.join(['| ' + ' | '.join(str(cell) for cell in row) + ' |' for row in table.values.tolist()]) + '\n\n'
                            output_file.write(header + separator + body)

                if page != book.pages[-1]:
                    output_file.write('---\n\n')
        LOG.info(f"翻译完成: {output_file_path}")






















