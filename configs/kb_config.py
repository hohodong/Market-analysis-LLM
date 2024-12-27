import os

# 默认使用的知识库
DEFAULT_KNOWLEDGE_BASE = "samples"

# 默认向量库/全文检索引擎类型
DEFAULT_VS_TYPE = "faiss"

# 缓存向量库数量（针对FAISS）
CACHED_VS_NUM = 1

# 缓存临时向量库数量（针对FAISS），用于文件对话
CACHED_MEMO_VS_NUM = 10

# 知识库中单段文本长度(不适用MarkdownHeaderTextSplitter)
CHUNK_SIZE = 250

# 知识库中相邻文本重合长度(不适用MarkdownHeaderTextSplitter)
OVERLAP_SIZE = 50

# 知识库匹配向量数量
VECTOR_SEARCH_TOP_K = 3

# 知识库匹配的距离阈值，一般取值范围在0-1之间，SCORE越小，距离越小进而相关度越高。
# 默认设为1，在WEBUI中调整范围为0-2
SCORE_THRESHOLD = 1.0

# 默认搜索引擎。可选：bing, duckduckgo, metaphor
DEFAULT_SEARCH_ENGINE = "duckduckgo"

# 搜索引擎匹配结题数量
SEARCH_ENGINE_TOP_K = 3


# Bing 搜索必备变量
BING_SEARCH_URL = "https://api.bing.microsoft.com/v7.0/search"


BING_SUBSCRIPTION_KEY = ""

# metaphor搜索需要KEY
METAPHOR_API_KEY = ""

# 心知天气 API KEY，用于天气Agent。申请：https://www.seniverse.com/
SENIVERSE_API_KEY = ""

# 是否开启中文标题加强，以及标题增强的相关配置
# 通过增加标题判断，判断哪些文本为标题，并在metadata中进行标记；
# 然后将文本与往上一级的标题进行拼合，实现文本信息的增强。
ZH_TITLE_ENHANCE = False

# PDF OCR 控制：只对宽高超过页面一定比例（图片宽/页面宽，图片高/页面高）的图片进行 OCR。
# 这样可以避免 PDF 中一些小图片的干扰，提高非扫描版 PDF 处理速度
PDF_OCR_THRESHOLD = (0.6, 0.6)

# 每个知识库的初始化介绍，用于在初始化知识库时显示和Agent调用，没写则没有介绍，不会被Agent调用。
KB_INFO = {
    "知识库名称": "知识库介绍",
    "samples": "关于本项目issue的解答",
}


# 通常情况下不需要更改以下内容

# 知识库默认存储路径
KB_ROOT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "knowledge_base")
if not os.path.exists(KB_ROOT_PATH):
    os.mkdir(KB_ROOT_PATH)
# 数据库默认存储路径。
# 如果使用sqlite，可以直接修改DB_ROOT_PATH；如果使用其它数据库，请直接修改SQLALCHEMY_DATABASE_URI。
DB_ROOT_PATH = os.path.join(KB_ROOT_PATH, "info.db")
SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_ROOT_PATH}"

# 可选向量库类型及对应配置
kbs_config = {
    "faiss": {
    },
}

# TextSplitter配置项
text_splitter_dict = {
    "ChineseRecursiveTextSplitter": {
        "source": "huggingface",   # 选择tiktoken则使用openai的方法
        "tokenizer_name_or_path": "",
    },
    "SpacyTextSplitter": {
        "source": "huggingface",
        "tokenizer_name_or_path": "gpt2",
    },
    "RecursiveCharacterTextSplitter": {
        "source": "tiktoken",
        "tokenizer_name_or_path": "cl100k_base",
    },
    "MarkdownHeaderTextSplitter": {
        "headers_to_split_on":
            [
                ("#", "head1"),
                ("##", "head2"),
                ("###", "head3"),
                ("####", "head4"),
            ]
    },
}

# TEXT_SPLITTER 名称
TEXT_SPLITTER_NAME = "ChineseRecursiveTextSplitter"

# Embedding模型定制词语的词表文件
EMBEDDING_KEYWORD_FILE = "embedding_keywords.txt"
