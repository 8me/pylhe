from setuptools import setup

extras_require = {
    "develop": [
        "check-manifest",
        "pyflakes",
        "pre-commit",
        "black;python_version>='3.6'",  # Black is Python3 only
        "twine",
    ],
}
extras_require["complete"] = sorted(set(sum(extras_require.values(), [])))

setup(
    extras_require=extras_require,
    use_scm_version=lambda: {"local_scheme": lambda version: ""},
)
