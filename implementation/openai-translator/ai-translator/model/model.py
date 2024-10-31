from book import ContentType

class Model:
    def make_text_prompt(self, text:str, target_lanuage:str)-> str:
        return f"翻译为{target_lanuage}: {text}"

    def make_table_prompt(self, table:str, targe_lanuage:str) -> str:
        return f"翻译为{targe_lanuage}, 以空格和换行符表示表格： \n{table}"

    def translate_prompt(self, content, target_lanuage:str) -> str:
        if content.content_type == ContentType.TEXT:
            return self.make_text_prompt(content.original, target_lanuage)
        elif content.content_type == ContentType.TABLE:
            return self.make_table_prompt(content.get_original_as_str(), target_lanuage)

        def make_request(self, prompt):
            raise NotImplementedError("子类必须实现 make_request 方法")