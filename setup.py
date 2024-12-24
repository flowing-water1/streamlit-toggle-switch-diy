import setuptools
import os

# 读取 README.md 内容
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamlit_toggle_switch_diy",
    version="1.0.3",
    author="Flow Water",
    author_email="1665526933@qq.com",
    description="Creates a customizable toggle, and you can change the label's background-color.",
    long_description=long_description,  # 设置长描述
    long_description_content_type="text/markdown",  # 指定内容类型为 Markdown
    url="https://github.com/sqlinsights/streamlit-toggle-switch",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        "streamlit_toggle_diy": [
            "frontend/build/**/*",
            "frontend/public/**/*",
        ],
    },
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
)
