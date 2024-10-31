import argparse

class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Translate English PDF book to Chinese.')
        self.parser.add_argument('--config', type=str, default='config.yaml', help='Configuration file with model and API setting.')
        self.parser.add_argument('--model_type', type=str, required=True, choices=['GLMModel', 'OpenAIModel'], help='The type of translation model to use, Chooser between "GLMModel" and "OpenAIModel".')
        self.parser.add_argument('--glm_model_url', type=str, help='The URL of the ChatGLM model URL.')
        self.parser.add_argument('--timeout', type=int, help='Timeout for API request in seconds.')
        self.parser.add_argument('--openai_model', type=str, help = 'The model name of OpenAI model. Required if model type is "OpenAIModel".')
        self.parser.add_argument('--openai_api_key', type=str, help = 'The API key for OpenAIModel. Reuired if model type is "OpenAIModel".')
        self.parser.add_argument('--book', type=str, help='PDF file to translate.')
        self.parser.add_argument('--file_format', type=str, help='The file format of translated book. Now supporting PDF and Mardown.')


    def parse_arguments(self):
        args = self.parser.parse_args()
        if args.model_type == 'OpenAIModel' and not args.openai_model and not args.openai_api_key:
            self.parser.error("--openai_model and --openai_apo_key is required when using OpenAIModel")
        return args