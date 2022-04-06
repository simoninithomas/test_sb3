from setuptools import setup

install_requires = [
    "huggingface_hub",
]

setup(
    name='huggingface_sb3_test',
    version='1.0.7',
     packages=['huggingface_sb3_test'],
    url='https://github.com/simoninithomas/test_sb3',
    license='Apache',
    author='Thomas Simonini, Omar Sanseviero and Hugging Face Team',
    author_email='thomas.simonini@huggingface.co',
    description='Additional code for Stable-baselines3 to load and upload models from the Hub.',
    install_requires=install_requires,
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="reinforcement learning deep reinforcement learning RL",
)


