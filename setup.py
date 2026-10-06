from setuptools import setup

setup(
    name="project-b-utils",
    version="2.0.0",
    packages=["project_b_utils"],
    package_dir={"project_b_utils": "src"},
    author="AslanI22",
    description="Утилиты для работы с датами и строками",
    python_requires=">=3.8",
)