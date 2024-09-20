# setup.py
from setuptools import setup, find_packages

setup(
    name="extrator_audio",
    version="0.1.0",
    description="Um pacote simples para extrair áudio de vídeos do YouTube",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    author="Joao Victor",
    author_email="jvdeitos@hotmail.com",
    url="https://github.com/joaovictordds/doau",
    packages=find_packages(),
    classifiers=[  # Certifique-se de que 'classifiers' está presente apenas uma vez
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["yt-dlp"],
)
