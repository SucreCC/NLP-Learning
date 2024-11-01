import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, ConfigLoader, LOG
from model import OpenAIModel
from flask import Flask, request, jsonify
from utils import ArgumentParser,ConfigLoader,LOG
from model import GLMModel, OpenAIModel
from translator import PDFTranslator

app = Flask(__name__)

# 定义接口
@app.route('/translate', methods=['POST'])
def translate():
    # 从请求体中获取参数
    data = request.get_json()
    print(data)
    return jsonify({"status": "success", "translation": "translation_result"})

    # # 从请求中获取参数，若为空则从配置文件中加载默认值
    # argument_parser = ArgumentParser()
    # args = argument_parser.parse_arguments()
    # config_loader = ConfigLoader(args.config)
    # config = config_loader.load_config()
    #
    # model_name = data.get("openai_model", config['OpenAIModel']['model'])
    # api_key = data.get("openai_api_key", config['OpenAIModel']['api_key'])
    # pdf_file_path = data.get("book", config['common']['book'])
    # file_format = data.get("file_format", config['common']['file_format'])
    #
    # # 初始化模型和翻译器
    # model = OpenAIModel(model=model_name, api_key=api_key)
    # translator = PDFTranslator(model)
    #
    # try:
    #     # 调用翻译功能
    #     translation_result = translator.translate_pdf(pdf_file_path, file_format)
    #
    #     # 返回翻译结果
    #     return jsonify({"status": "success", "translation": translation_result})
    # except Exception as e:
    #     # 返回错误信息
    #     return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)












# if __name__ == "__main__":
#     argument_parser = ArgumentParser()
#     args = argument_parser.parse_arguments()
#     config_loader = ConfigLoader(args.config)
#     config = config_loader.load_config()
#
#     model_name = args.openai_model if args.openai_model else config['OpenAIModel']['model']
#     api_key = args.openai_api_key if args.openai_api_key else config['OpenAIModel']['api_key']
#     model = OpenAIModel(model=model_name, api_key=api_key)
#
#     pdf_file_path = args.book if args.book else config['common']['book']
#     file_format = args.file_format if args.file_format else config['common']['file_format']
#
#     translator = PDFTranslator(model)
#     translator.translate_pdf(pdf_file_path, file_format)