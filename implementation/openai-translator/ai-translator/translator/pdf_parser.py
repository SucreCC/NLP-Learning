import pdfplumber
import re
from typing import Optional
from book import Book, Page, Content, ContentType, TableContent
from translator.exceptions import PageOutOfRangeException
from utils import LOG


class PDFParser:
    def __init__(self):
        pass

    def parse_pdf(self, pdf_file_path:str, pages:Optional[int] = None) -> Book:
        book = Book(pdf_file_path)

        with pdfplumber.open(pdf_file_path) as pdf:
            if pages is not None and pages > len(pdf.pages):
                raise PageOutOfRangeException(len(pdf.pages), pages)

            if pages is None:
                pages_to_parse = pdf.pages
            else:
                pages_to_parse = pdf.pages[:pages]

            for pdf_page in pages_to_parse:
                page = Page()

                raw_text = pdf_page.extract_text()
                tables = pdf_page.extract_tables()


                # for table_data in tables:
                #     for row in table_data:
                #         for cell in row:
                #             raw_text = raw_text.replace(cell, "", 1)

                for table_data in tables:
                    for row in table_data:
                        for cell in row:
                            cell_text = re.escape(cell.strip())  # 去除多余的空格并转义特殊字符

                            # 使用正则表达式找到第一个匹配项
                            match = re.search(cell_text, raw_text)
                            if match:
                                # 找到匹配的开始和结束位置
                                start_idx = match.start()
                                end_idx = match.end()

                                # 删除该位置的 cell_text
                                raw_text = raw_text[:start_idx] + raw_text[end_idx:]


                if raw_text:
                    raw_text_lines = raw_text.splitlines()
                    cleaned_raw_text_lines = [line.strip() for line in raw_text_lines if line.strip()]
                    cleaned_raw_text = "\n".join(cleaned_raw_text_lines)
                    text_content = Content(content_type=ContentType.TEXT, original=cleaned_raw_text)
                    page.add_content(text_content)
                    LOG.debug(f"[raw_text]\n {cleaned_raw_text}")
                    tables


                if tables:
                    table = TableContent(tables)
                    page.add_content(table)
                    LOG.debug(f"[table]\n{table}")

                book.add_page(page)

        return book
